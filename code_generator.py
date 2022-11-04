import os
import inspect
from typing import Dict
from code_generator.templates import *

from models import user as User, Order


def generate_entity(class_model: type) -> None:
    filename = f'src/domain/entities/{class_model.__name__.lower()}.py'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    open('src/domain/entities/__init__.py', 'a').close()

    attributes: Dict[str, type] = inspect.getmembers(class_model())[0][1]
    with open(filename, 'w+') as f:
        f.write(imports_entity)

        for _, type_of_field in attributes.items():
            if type_of_field.__module__ == "builtins":
                continue
            f.write(
                f'from {type_of_field.__module__} import {type_of_field.__name__}\n')

        f.write(f"""\n\n@dataclass(frozen=True)
class {class_model.__name__.capitalize()}:
    id: uuid""")

        for field, type_of_field in attributes.items():
            if field == "id":
                continue

            f.write(
                f"""
    {field}: {type_of_field.__name__}""")
        f.write("\n")


def generate_entities(list_of_models: list):
    set(map(generate_entity, list_of_models))


generate_entities([User, Order])


def generate_model(class_model: type) -> None:
    filename = f'src/infra/models.py'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    open('src/infra/__init__.py', 'a').close()

    attributes: Dict[str, type] = inspect.getmembers(class_model())[0][1]
    with open(filename, 'w+') as f:
        f.write('# -*- coding: utf-8 -*-\n')
        for _, type_of_field in attributes.items():
            if type_of_field.__module__ == "builtins" or type_of_field.__name__ == 'datetime':
                continue
            f.write(
                f'from {type_of_field.__module__} import {type_of_field.__name__}')

        f.write(template_model)
        f.write(f"""class {class_model.__name__.capitalize()}Model:
    __tablename__ = "{class_model.__name__.lower()}s"

    id: str = Column(String(255), primary_key=True, index=True)""")

        for field, type_of_field in attributes.items():
            if field in ("id", "created_at", "updated_at"):
                continue

            f.write(f"""
    {field}: {type_of_field.__name__} = Column({convert_to_sqlalchemy_type(type_of_field)})""")

        f.write(timestamp_model)


def convert_to_sqlalchemy_type(type: type) -> str:
    match type.__name__:
        case 'str':
            return 'String(255)'
        case 'bool':
            return 'Boolean()'
        case 'int':
            return 'Integer()'
        case 'float':
            return 'Float()'
        case 'datetime':
            return 'DateTime()'



generate_model(User)
