import os
import inspect
from typing import Dict

from models import User, Order


def generate_entity(class_model: type) -> None:
    filename = f'entities/{class_model.__name__.lower()}.py'
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    attributes: Dict[str, type] = inspect.getmembers(class_model())[0][1]
    with open(filename, 'w+') as f:
        f.write(f"""# -*- coding: utf-8 -*-
from uuid import UUID as uuid
from dataclasses import dataclass\n""")

        for _, type_of_field in attributes.items():
            if type_of_field.__module__ == "builtins":
                continue
            f.write(f'from {type_of_field.__module__} import {type_of_field.__name__}\n')

        f.write(f"""\n\n@dataclass(frozen=True)
class {class_model.__name__}:
    id: uuid""")

        for field, type_of_field in attributes.items():
            if field == "id":
                continue

            f.write(
                f"""
    {field}: {type_of_field.__name__}""")
        f.write("\n")


generate_entity(User)
generate_entity(Order)
