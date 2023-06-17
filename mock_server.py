from code_generator.domain.entities import generate_entity
from code_generator.seedwork.domain import generate_domain_seedwork
from code_generator.seedwork.application import generate_use_cases
from code_generator.domain.repositories import (
    generate_repository as generate_domain_repository,
)
from code_generator.infra.models import generate_model
from code_generator.infra.repositories import generate_repository
from code_generator.application import generate_routers
from code_generator.main import generate_main
from base_request import Entity, EntityItem, convert_entity_type


def build_api_service(entities: list[Entity]):
    generate_domain_seedwork()
    generate_use_cases()

    for entity in entities:
        for item in entity.items:
            item.type = convert_entity_type(item.type)

        generate_entity(entity.name, entity.items)
        generate_domain_repository(entity.name)
        generate_repository(entity.name, entity.items)
        generate_model(entity.name, entity.items)
        generate_routers(entity.name, entity.items)

    generate_main([entity.name for entity in entities])


user_items = [EntityItem(name="name", type="str")]
user = Entity(name="user", items=user_items)


product_items = [
    EntityItem(name="name", type="str"),
    EntityItem(name="valid_date", type="datetime"),
    EntityItem(name="quantity", type="int", has_default_value=True, default_value=10),
    EntityItem(name="weight", type="float", has_default_value=True, default_value=0.0),
    EntityItem(
        name="description",
        type="str",
        has_default_value=True,
        default_value="no description",
    ),
    EntityItem(name="active", type="bool", has_default_value=True, default_value=False),
    EntityItem(name="user", type="user"),
]

product = Entity(name="product", items=product_items)

build_api_service([product, user])
