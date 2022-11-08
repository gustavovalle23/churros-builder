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
    print(dict(default_values))


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
            default_value = f" = {default_values.get(field)}" if default_values.get(field, "kosv") != "kosv" else ""
            if field == "id":
                continue

            f.write(
                f"""
    {field}: {type_of_field.__name__}{default_value}""")
        f.write("\n")


def generate_entities(list_of_models: list):
    set(map(generate_entity, list_of_models))
