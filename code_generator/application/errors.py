import os
import inspect
from typing import Dict


def generate_errors(class_model: type) -> None:
    filename = f'src/application/errors/{class_model.__name__.lower()}.py'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    open('src/application/errors/__init__.py', 'a').close()

    attributes: Dict[str, type] = inspect.getmembers(class_model())[0][1]
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
