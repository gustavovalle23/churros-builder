from pydantic import BaseModel
from typing import Optional, Any

builtins_types = ['str', 'int', 'float', 'bool']

class EntityItem(BaseModel):
    name: str
    type: str
    default_value: Optional[Any]

class Entity(BaseModel):
    entity_name: str
    items: list[EntityItem]