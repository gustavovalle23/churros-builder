import questionary
from typing import Dict, Any
import inspect


def transform_type(type: str) -> type:
    types = {"String": str, "Float": float, "Boolean": bool, "Integer": int}
    return types.get(type)


# Entity Name
entity_name = questionary.text("What's the entity name?").ask()
attributes: Dict[str, Any] = {}

# Attributes
next_attribute = True
while next_attribute:
    attribute_name = questionary.text("What's the attribute name?").ask()
    attribute_type = questionary.select(
        "What's the attribute type?",
        choices=["Boolean", "String", "Float", "Integer"],
    ).ask()

    attributes[attribute_name] = transform_type(attribute_type)
    next_attribute = questionary.confirm(
        "There are next attribute?", default=False
    ).ask()


Entity = type(entity_name, (), {})

for attribute, type in attributes.items():
    Entity.__annotations__[attribute] = type
