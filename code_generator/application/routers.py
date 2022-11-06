import os


def generate_routers(class_model: type) -> None:
    from code_generator.application.errors import generate_errors
    from code_generator.application.dtos import generate_dtos

    generate_errors(class_model)
    generate_dtos(class_model)

    model_name_min = class_model.__name__.lower()
    model_name = f'{class_model.__name__.capitalize()}'

    filename = f'src/application/routers/{model_name_min}.py'
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open('src/application/routers/__init__.py', 'a') as f:
        f.write(f'from src.application.routers.{model_name_min} import router as router_{model_name_min}s\n')

    with open(filename, 'w+') as f:
        f.write(f"""# -*- coding: utf-8 -*-
from typing import Tuple, Optional
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status

from src.domain.entities.{model_name_min} import {model_name}
from src.application.dtos.{model_name_min} import Create{model_name}Input, Update{model_name}Input
from src.application.errors.{model_name_min} import {model_name}NotFound
from src.infra.models import get_db
from src.infra.repositories import {model_name_min} as {model_name_min}_repository

router = APIRouter()

@router.get("/{model_name_min}s", tags=["{model_name_min}s"])
async def find_{model_name_min}s(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    {model_name_min}s: Tuple[{model_name}] = {model_name_min}_repository.find_all(db, skip, limit)
    return {'{'}"{model_name_min}s": {model_name_min}s{'}'}


@router.get("/{model_name_min}s/{'{'}{model_name_min}_id{'}'}", tags=["{model_name_min}s"])
async def find_{model_name_min}({model_name_min}_id: str, db: Session = Depends(get_db)):
    {model_name_min}: Optional[{model_name}] = {model_name_min}_repository.find_by_id(db, {model_name_min}_id)
    if not {model_name_min}:
        return {model_name}NotFound()
    return {'{'}"{model_name_min}": {model_name_min}{'}'}


@router.post("/{model_name_min}s", tags=["{model_name_min}s"], status_code=status.HTTP_201_CREATED)
async def create_{model_name_min}({model_name_min}: Create{model_name}Input, db: Session = Depends(get_db)):
    {model_name_min}_created = {model_name_min}_repository.save(db, {model_name_min})
    return {'{'}"{model_name_min}": {model_name_min}_created{'}'}


@router.patch("/{model_name_min}s", tags=["{model_name_min}s"])
async def update_{model_name_min}(input: Update{model_name}Input, db: Session = Depends(get_db)):
    {model_name_min}: Optional[{model_name}] = {model_name_min}_repository.find_by_id(db, input.id)
    if not {model_name_min}:
        return {model_name}NotFound()

    updated_{model_name_min} = {model_name_min}_repository.update(db, input)
    return {'{'}"message": "updated", {model_name_min}: updated_{model_name_min}{'}'}


@router.delete("/{model_name_min}s/{'{'}{model_name_min}_id{'}'}", tags=["{model_name_min}s"])
async def delete_{model_name_min}(
    {model_name_min}_id: str,
    db: Session = Depends(get_db)
):
    {model_name_min}: Optional[{model_name}] = {model_name_min}_repository.find_by_id(db, {model_name_min}_id)
    if not {model_name_min}:
        return {model_name}NotFound()

    {model_name_min}_repository.delete(db, {model_name_min}_id)
    return {'{'}"message": "deleted"{'}'}
""")
