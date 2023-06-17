import os
from typing import Any

from base_request import EntityItem, builtins_types
from code_generator.common.templates import imports_entity

check_if_required = lambda attribute: not attribute.default_value
check_if_not_required = lambda attribute: attribute.default_value


def generate_entity(entity_name: str, entity_items: list[EntityItem]) -> None:
    filename = f"src/{entity_name}/domain/entities.py"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    open(f"src/{entity_name}/domain/__init__.py", "a").close()


    with open(filename, "w+") as f:
        f.write(imports_entity)

        for attribute in entity_items:
            if attribute.type in builtins_types:
                continue
            f.write(
                f"""from {attribute.type} import {attribute.type}\n"""
            )

        f.write("\nfrom src.__seedwork.domain.entities import Entity\n")
        f.write(
            f"""\n\n@dataclass(kw_only=True, frozen=True, slots=True)
class {entity_name.capitalize()}(Entity):
    id: int"""
        )

        default_attributes: list[EntityItem] = list(filter(check_if_not_required, entity_items))
        required_attributes: list[EntityItem] = list(filter(check_if_required, entity_items))

        for required_attribute in required_attributes:
            field = required_attribute.name
            type_of_field = required_attribute.type

            if field == "id":
                continue

            f.write(
                f"""
    {field}: {type_of_field}"""
            )

        for default_attribute in default_attributes:
            field = default_attribute.name
            type_of_field = default_attribute.type

            if field == "id":
                continue

            f.write(
                f"""
    {field}: Optional[{type_of_field}] = '{default_attribute.default_value}'"""
            )

        f.write(
            """\n
    def __post_init__(self):
        if not self.created_at:
            self._set('created_at',  datetime.now(
                timezone.utc))
"""
        )


def generate_entities(list_of_models: list) -> set:
    return set(map(generate_entity, list_of_models))


generate_entity('user', [EntityItem(name='name', type='str', default_value='Gus')])
