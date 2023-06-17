from code_generator.domain.entities import generate_entity
from code_generator.seedwork.domain import generate_domain_seedwork
from code_generator.seedwork.application import generate_use_cases
from code_generator.domain.repositories import generate_repository
from code_generator.infra.models import generate_model
from code_generator.infra.repositories import generate_repository
from code_generator.application import generate_routers
from code_generator.main import generate_main
from base_request import Entity, EntityItem


def build_api_service(entity: Entity):
    generate_domain_seedwork()
    generate_use_cases()
    generate_entity(entity.name, entity.items)
    generate_repository(entity.name, entity.items)
    generate_model(entity.name, entity.items)
    generate_routers(entity.name, entity.items)
    generate_main([entity.name])


items = [
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
]
entity = Entity(name="product", items=items)
build_api_service(entity)
