import os
import inspect
from typing import Dict, List, Any

from code_generator.common.templates import (
    timestamp_model, template_model
)


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


filename = 'src/infra/models.py'


def generate_model(class_model: type, multiple_model) -> None:
    if not os.path.exists(filename):
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        open('src/infra/__init__.py', 'a').close()
        with open(filename, 'a+') as f:
            f.write('# -*- coding: utf-8 -*-\n')

    attributes: List[Dict[str, Any]] = inspect.getmembers(class_model())[0][1]["attributes"]

    with open(filename, 'a+') as f:
        for attribute in attributes:
            type_of_field = attribute.get("type")
            if type_of_field.__module__ == "builtins" or type_of_field.__name__ == 'datetime':
                continue

            f.write(
                f'from {type_of_field.__module__} import {type_of_field.__name__}')

        if not multiple_model:
            f.write(template_model)

        f.write(f"""\n\nclass {class_model.__name__.capitalize()}Model(Base):
    __tablename__ = "{class_model.__name__.lower()}s"

    id: str = Column(String(255), primary_key=True, index=True)""")

        for attribute in attributes:
            field = attribute.get("name")
            type_of_field = attribute.get("type")

            if field in ("id", "created_at", "updated_at"):
                continue

            f.write(f"""
    {field}: {type_of_field.__name__} = Column({convert_to_sqlalchemy_type(type_of_field)})""")

        f.write(timestamp_model)


def generate_models(list_of_models):
    if os.path.exists(filename):
        os.remove(filename)

    multiple_model = False
    for model in list_of_models:
        generate_model(model, multiple_model)
        multiple_model = True
