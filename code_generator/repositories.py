import os
import inspect
from typing import Dict

from code_generator.common.templates import *


def generate_repository(class_model: type) -> None:
    filename = f'src/infra/repositories/{class_model.__name__.lower()}.py'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    open('src/infra/repositories/__init__.py', 'a').close()

    model_name = f'{class_model.__name__.capitalize()}'

    attributes: Dict[str, type] = inspect.getmembers(class_model())[0][1]
    with open(filename, 'w+') as f:
        f.write(imports_repository)

        f.write(f"""
from src.domain.entities.{class_model.__name__.lower()} import {model_name}
from src.infra.models import {model_name}Model
""")


        f.write(f"""\n
def to_entity(model: Query | {model_name}Model) -> {model_name} | None:
    if not model:
        return

    return {model_name}(\n""")

        for field, _ in attributes.items():
            f.write(f"""        model.{field},\n""")
        f.write(f"""    )\n\n
def find_all(db: Session, skip: int = 0, limit: int = 100) -> List[{model_name}]:
    {class_model.__name__.lower()}s = (
        db.query({model_name}Model).offset(skip).limit(limit)
    )
    return tuple(map(to_entity, {class_model.__name__.lower()}s))


def find_by_id(db: Session, {class_model.__name__.lower()}_id: str) -> {model_name} | None:
    {class_model.__name__.lower()} = (
        db.query({model_name}Model)
        .filter({model_name}Model.id == {class_model.__name__.lower()}_id)
        .first()
    )
    return to_entity({class_model.__name__.lower()})


def delete(db: Session, {class_model.__name__.lower()}_id: str) -> None:
    db.query({model_name}Model).filter({model_name}Model.id == {class_model.__name__.lower()}_id).delete()
    db.commit()
""")
