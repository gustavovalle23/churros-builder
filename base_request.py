from pydantic import BaseModel
from typing import Optional, Any

builtins_types = ["str", "int", "float", "bool"]


def convert_entity_type(name: str) -> str:
    if name in builtins_types:
        return name
    if name == "datetime":
        return name

    return name.capitalize()


class EntityItem(BaseModel):
    name: str
    type: str
    default_value: Optional[Any]
    has_default_value: Optional[bool] = False


class Entity(BaseModel):
    name: str
    items: list[EntityItem]
