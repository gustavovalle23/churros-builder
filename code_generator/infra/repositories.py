import os
import inspect
from typing import Dict

from code_generator.common.templates import *


def generate_repository(class_model: type) -> None:
    filename = f'src/infra/repositories/{class_model.__name__.lower()}.py'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    open('src/infra/repositories/__init__.py', 'a').close()

    model_name = f'{class_model.__name__.capitalize()}'
    model_name_min = f'{class_model.__name__.lower()}'

    attributes: Dict[str, type] = inspect.getmembers(class_model())[0][1]
    with open(filename, 'w+') as f:
        f.write(imports_repository)

        f.write(f"""
from src.application.dtos.{model_name_min} import Create{model_name}Input, Update{model_name}Input
from src.domain.entities.{model_name_min} import {model_name}
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
    {model_name_min}s = (
        db.query({model_name}Model).offset(skip).limit(limit)
    )
    return tuple(map(to_entity, {model_name_min}s))


def find_by_id(db: Session, {model_name_min}_id: str) -> {model_name} | None:
    {model_name_min} = (
        db.query({model_name}Model)
        .filter({model_name}Model.id == {model_name_min}_id)
        .first()
    )
    return to_entity({model_name_min})


def delete(db: Session, {model_name_min}_id: str) -> None:
    db.query({model_name}Model).filter({model_name}Model.id == {model_name_min}_id).delete()
    db.commit()


def save(db: Session, input: Create{model_name}Input) -> {model_name} | None:
    {model_name_min} = {model_name}Model(
        id=uuid().hex, **json.loads(input.json())
    )
    db.add({model_name_min})
    db.commit()
    return to_entity({model_name_min})


def update(db: Session, input: Update{model_name}Input) -> {model_name} | None:
    {model_name_min}_id = input.id
    data: dict = json.loads(input.json())
    data = {'{'}attribute: value for attribute, value in data.items() if value != None and attribute != 'id'{'}'}

    db.query({model_name}Model).filter({model_name}Model.id == {model_name_min}_id).update(
        data
    )
    db.commit()
    updated_{model_name_min} = db.query({model_name}Model).filter({model_name}Model.id == input.id).first()
    return to_entity(updated_{model_name_min})
""")
