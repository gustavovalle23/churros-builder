import os

from base_request import EntityItem


def generate_errors(entity_name: str, items: list[EntityItem]) -> None:
    filename = f'src/{entity_name}/application/errors.py'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    open(f'src/{entity_name}/application/__init__.py', 'a').close()

    with open(filename, 'w+') as f:
        f.write(f"""# -*- coding: utf-8 -*-
from fastapi import status, HTTPException


class {entity_name.capitalize()}NotFound:
    def __init__(self) -> None:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            [
                {'{'}
                    "loc": ["param", "{entity_name}_id"],
                    "msg": "{entity_name.capitalize()} not found",
                    "type": "not_found_error",
                {'}'}
            ],
        )
""")
