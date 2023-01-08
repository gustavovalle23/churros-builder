import os
import inspect
from typing import Dict

from code_generator.common.templates import imports_entity

check_if_required = lambda attribute: "default_value" not in attribute.keys()
check_if_not_required = lambda attribute: "default_value" in attribute.keys()


def generate_entity(class_model: type) -> None:
    filename = f"src/{class_model.__name__.lower()}/domain/entities.py"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    open(f"src/{class_model.__name__.lower()}/domain/__init__.py", "a").close()

    members = inspect.getmembers(class_model())
    attributes: Dict[str, type] = members[0][1]["attributes"]

    with open(filename, "w+") as f:
        f.write(imports_entity)

        for attribute in attributes:
            if attribute.get("type").__module__ == "builtins":
                continue
            f.write(
                f"""from {attribute.get('type').__module__} import {attribute.get('type').__name__}\n"""
            )

        f.write("\nfrom src.__seedwork.domain.entities import Entity\n")
        f.write(
            f"""\n\n@dataclass(kw_only=True, frozen=True, slots=True)
class {class_model.__name__.capitalize()}(Entity):
    id: uuid"""
        )

        default_attributes = list(filter(check_if_not_required, attributes))
        required_attributes = list(filter(check_if_required, attributes))

        for required_attribute in required_attributes:
            field = required_attribute.get("name")
            type_of_field = required_attribute.get("type")

            if field == "id":
                continue

            f.write(
                f"""
    {field}: {type_of_field.__name__}"""
            )

        for default_attribute in default_attributes:
            field = default_attribute.get("name")
            type_of_field = default_attribute.get("type")

            if field == "id":
                continue

            f.write(
                f"""
    {field}: Optional[{type_of_field.__name__}] = {default_attribute.get('default_value')}"""
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
