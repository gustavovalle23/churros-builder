import os
import inspect
from typing import Dict

from code_generator.common.templates import *


def generate_entity(class_model: type) -> None:
    filename = f'src/domain/entities/{class_model.__name__.lower()}.py'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    open('src/domain/entities/__init__.py', 'a').close()

    members = inspect.getmembers(class_model())
    attributes: Dict[str, type] = members[0][1]
    default_values = dict(members[members.index(('__weakref__', None))+1::])

    with open(filename, 'w+') as f:
        f.write(imports_entity)

        for _, type_of_field in attributes.items():
            if type_of_field.__module__ == "builtins":
                continue
            f.write(
                f'from {type_of_field.__module__} import {type_of_field.__name__}\n')

        f.write(f"""\n\n@dataclass(kw_only=True, frozen=True, slots=True)
class {class_model.__name__.capitalize()}:
    id: uuid""")

        default_attributes = {
            k: v for k, v in attributes.items() if k in default_values.keys()
        }

        required_attributes = {
            k: v for k, v in attributes.items() if k not in default_values.keys()
        }

        for field, type_of_field in required_attributes.items():
            if field == "id":
                continue

            f.write(
                f"""
    {field}: {type_of_field.__name__}""")

        for field, type_of_field in default_attributes.items():
            if field == "id":
                continue

            f.write(
                f"""
    {field}: Optional[{type_of_field.__name__}] = {default_values.get(field)}""")

        f.write("""\n
    def __post_init__(self):
        if not self.created_at:
            self._set('created_at',  datetime.now(
                timezone.utc))
""")


def generate_entities(list_of_models: list):
    set(map(generate_entity, list_of_models))
