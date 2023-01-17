import questionary
from typing import Dict, Any, List
from code_generator.domain.entities import generate_entities
from code_generator.domain.repositories import generate_repositories
from code_generator.infra.models import generate_models
from code_generator.infra.repositories import generate_repository
from code_generator.application import generate_routers
from code_generator.main import generate_main
from code_generator.seedwork.domain import generate_domain_seedwork
from code_generator.seedwork.application import generate_use_cases


def transform_type(type: str) -> type:
    types = {"String": str, "Float": float, "Boolean": bool, "Integer": int}
    return types.get(type)


attributes: List[Dict[str, Any]] = []
next_attribute = True

# entity_name = questionary.text("What's the entity name?").ask()

# while next_attribute:
#     attribute_name = questionary.text("What's the attribute name?").ask()
#     attribute_type = questionary.select(
#         "What's the attribute type?",
#         choices=["Boolean", "String", "Float", "Integer"],
#     ).ask()

#     has_default_value = questionary.confirm(
#         "There are a default value?", default=False
#     ).ask()

#     if has_default_value:
#         default_value = questionary.text("What's the default value?").ask()
#     else:
#         default_value = None

#     attributes.append(
#         {
#             "name": attribute_name,
#             "type": transform_type(attribute_type),
#             "default_value": default_value,
#             "has_default_value": has_default_value,
#         }
#     )

#     next_attribute = questionary.confirm(
#         "There are next attribute?", default=False
#     ).ask()


# Saved it for example tests
entity_name = "User"
from datetime import datetime
attributes = [
    {"name": "id", "type": int},
    {"name": "name", "type": str},
    {"name": "email", "type": str},
    {"name": "password", "type": str},
    {"name": "active", "type": bool, "default_value": False},
    {"name": "birth_date", "type": datetime},
    {"name": "height", "type": float, "default_value": 1.2},
]


Entity = type(entity_name, (), {})

Entity.__churrosoptions__ = {}
Entity.__churrosoptions__["attributes"] = attributes

generate_entities([Entity])
generate_repositories([Entity])
generate_models([Entity])
generate_repository(Entity)
generate_routers(Entity)
generate_main([Entity])
generate_domain_seedwork()
generate_use_cases()
