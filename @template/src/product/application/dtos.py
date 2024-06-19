# -*- coding: utf-8 -*-
from pydantic import BaseModel
from datetime import datetime
from src.user.application.dtos import User


class Product(BaseModel):
    id: int
    name: str
    valid_date: datetime
    quantity: int
    weight: float
    description: str
    active: bool
    user: User


class CreateProductInput(BaseModel):
    id: int
    name: str
    valid_date: datetime
    quantity: int
    weight: float
    description: str
    active: bool
    user: User


class UpdateProductInput(BaseModel):
    name: str
    valid_date: datetime
    quantity: int
    weight: float
    description: str
    active: bool
    user: User
