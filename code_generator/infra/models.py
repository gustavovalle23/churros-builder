import os

from base_request import EntityItem, builtins_types
from code_generator.common.templates import (
    timestamp_model,
    template_model,
    template_schema,
)


def convert_to_sqlalchemy_type(type: type) -> str:
    match type:
        case "str":
            return "String(255)"
        case "bool":
            return "Boolean()"
        case "int":
            return "Integer()"
        case "float":
            return "Float()"
        case "datetime":
            return "DateTime()"


models_filename = "src/infra/models.py"


def generate_model(entity_name: str, items: list[EntityItem]) -> None:
    if not os.path.exists(models_filename):
        os.makedirs(os.path.dirname(models_filename), exist_ok=True)
        open("src/infra/__init__.py", "a").close()
        with open(models_filename, "a+") as f:
            f.write(template_model)

    filename = f"src/infra/schemas/{entity_name}.py"

    if not os.path.exists(filename):
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        open("src/infra/schemas/__init__.py", "a").close()
        with open(filename, "a+") as f:
            f.write(template_schema)

    with open(filename, "a+") as f:
        for attribute in items:
            type_of_field = attribute.type
            if type_of_field in builtins_types or type_of_field == "datetime":
                continue

            if attribute.type == "datetime":
                f.write(f"""from datetime import datetime\n""")
            else:
                f.write(
                    f"""from src.{attribute.type.lower()}.domain.entities import {attribute.type.capitalize()}\n"""
                )

        f.write(
            f"""\n\nclass {entity_name.capitalize()}Model(Base):
    __tablename__ = "{entity_name}s"

    id: str = Column(String(255), primary_key=True, index=True)"""
        )

        for attribute in items:
            field = attribute.name
            type_of_field = attribute.type

            if field in ("id", "created_at", "updated_at"):
                continue

            if convert_to_sqlalchemy_type(type_of_field) is None:
                f.write(
                    f"""
    {field}_id = Column(Integer, ForeignKey('{field}s.id'))
    {field} = relationship('{field.capitalize()}', backref='products')"""
                )

            else:
                f.write(
                    f"""
    {field}: {type_of_field} = Column({convert_to_sqlalchemy_type(type_of_field)})"""
                )

        f.write(timestamp_model)
