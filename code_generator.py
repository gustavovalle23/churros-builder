from typing import Dict
import inspect
from models import User
import os

def convert_to_type(value: type):
    if issubclass(value, str):
        return 'str'

    if issubclass(value, float):
        return 'float'


def generate_entity(class_model: type):
    filename = f'entities/{class_model.__name__.lower()}.py'
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    attributes: Dict[str, type] = inspect.getmembers(class_model())[0][1]
    with open(filename, 'w+') as f:
        f.write(f"""# -*- coding: utf-8 -*-
class {class_model.__name__}:""")

        for field, value in attributes.items():
            type_field = convert_to_type(value)
            f.write(
f"""
    def get_{field}(self) -> {type_field}:
        return self._{field}
""")

generate_entity(User)
