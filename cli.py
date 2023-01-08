import questionary
from typing import Dict, Any, List
from code_generator.domain.entities import generate_entities


def transform_type(type: str) -> type:
    types = {"String": str, "Float": float, "Boolean": bool, "Integer": int}
    return types.get(type)


attributes: List[Dict[str, Any]] = []
next_attribute = True

entity_name = questionary.text("What's the entity name?").ask()

while next_attribute:
    attribute_name = questionary.text("What's the attribute name?").ask()
    attribute_type = questionary.select(
        "What's the attribute type?",
        choices=["Boolean", "String", "Float", "Integer"],
    ).ask()
    default_value = questionary.text("What's the default value?").ask()

    attributes.append(
        {
            "name": attribute_name,
            "type": transform_type(attribute_type),
            "default_value": default_value,
        }
    )

    next_attribute = questionary.confirm(
        "There are next attribute?", default=False
    ).ask()


# Saved it for example tests
# entity_name = "User"
# from datetime import datetime
# attributes = [
#     {"name": "id", "type": int},
#     {"name": "name", "type": str},
#     {"name": "email", "type": str},
#     {"name": "password", "type": str},
#     {"name": "active", "type": bool, "default_value": False},
#     {"name": "birth_date", "type": datetime},
#     {"name": "height", "type": float, "default_value": 1.2},
# ]


Entity = type(entity_name, (), {})

Entity.__churrosoptions__ = {}
Entity.__churrosoptions__["attributes"] = attributes

generate_entities([Entity])
