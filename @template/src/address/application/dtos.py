# -*- coding: utf-8 -*-
from pydantic import BaseModel


class Address(BaseModel):
    id: int
    street: str


class CreateAddressInput(BaseModel):
    id: int
    street: str


class UpdateAddressInput(BaseModel):
    street: str