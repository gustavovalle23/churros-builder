import questionary
from typing import Dict, Any
import inspect


def transform_type(type: str) -> type:
    types = {"String": str, "Float": float, "Boolean": bool, "Integer": int}
    return types.get(type)


attributes: Dict[str, Any] = {}

# Entity Name
entity_name = questionary.text("What's the entity name?").ask()

# Attributes
next_attribute = True
while next_attribute:
    attribute_name = questionary.text("What's the attribute name?").ask()
    attribute_type = questionary.select(
        "What's the attribute type?",
        choices=["Boolean", "String", "Float", "Integer"],
    ).ask()
    default_value = questionary.text("What's the default value?").ask()

    attributes[attribute_name] = {
        "type": transform_type(attribute_type),
        "default_value": default_value,
    }

    next_attribute = questionary.confirm(
        "There are next attribute?", default=False
    ).ask()


Entity = type(entity_name, (), {})

Entity.__churrosoptions__ = {}
Entity.__churrosoptions__["attributes"] = {}


for attribute, options in attributes.items():
    Entity.__churrosoptions__["attributes"]["name"] = attribute
    Entity.__churrosoptions__["attributes"]["type"] = options.get("type")
    Entity.__churrosoptions__["attributes"]["default_value"] = options.get(
        "default_value"
    )
