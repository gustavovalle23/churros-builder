import os
import inspect
from typing import Dict

from code_generator.common.templates import *


def generate_dtos(class_model: type) -> None:
    filename = f'src/application/dtos/{class_model.__name__.lower()}.py'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    open('src/application/dtos/__init__.py', 'a').close()

    attributes: Dict[str, type] = inspect.getmembers(class_model())[0][1]
    with open(filename, 'w+') as f:
        f.write("""# -*- coding: utf-8 -*-
from pydantic import BaseModel
from uuid import UUID as uuid
""")

        # Model
        for _, type_of_field in attributes.items():
            if type_of_field.__module__ == "builtins":
                continue
            f.write(
                f'from {type_of_field.__module__} import {type_of_field.__name__}\n')

        f.write(f"""\n
class {class_model.__name__.capitalize()}(BaseModel):
    id: uuid""")

        for field, type_of_field in attributes.items():
            if field == "id":
                continue

            f.write(
                f"""
    {field}: {type_of_field.__name__}""")


        # Create Model Input
        f.write(f"""\n\n
class Create{class_model.__name__.capitalize()}Input(BaseModel):
    id: uuid""")

        for field, type_of_field in attributes.items():
            if field == "id":
                continue

            f.write(
                f"""
    {field}: {type_of_field.__name__}""")




        # Update Model Input
        f.write(f"""\n\n
class Update{class_model.__name__.capitalize()}Input(BaseModel):""")

        for field, type_of_field in attributes.items():
            if field == "id":
                continue

            f.write(
                f"""
    {field}: {type_of_field.__name__}""")
        f.write("\n")


