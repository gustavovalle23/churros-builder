import os


def generate_errors(class_model: type) -> None:
    filename = f'src/{class_model.__name__.lower()}/application/errors.py'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    open(f'src/{class_model.__name__.lower()}/application/__init__.py', 'a').close()

    with open(filename, 'w+') as f:
        f.write(f"""# -*- coding: utf-8 -*-
from fastapi import status, HTTPException


class {class_model.__name__.capitalize()}NotFound:
    def __init__(self) -> None:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            [
                {'{'}
                    "loc": ["param", "{class_model.__name__.lower()}_id"],
                    "msg": "{class_model.__name__.capitalize()} not found",
                    "type": "not_found_error",
                {'}'}
            ],
        )
""")
