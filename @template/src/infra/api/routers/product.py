# -*- coding: utf-8 -*-
from typing import Tuple, Optional
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status

from src.infra.models import get_db
from src.product.domain.entities import Product
from src.product.application.dtos import CreateProductInput, UpdateProductInput
from src.product.application.errors import ProductNotFound
from src.infra.repositories import product as product_repository

router = APIRouter()

@router.get("/products", tags=["products"])
async def find_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    products: Tuple[Product] = product_repository.find_all(db, skip, limit)
    return {"products": products}


@router.get("/products/{product_id}", tags=["products"])
async def find_product(product_id: str, db: Session = Depends(get_db)):
    product: Optional[Product] = product_repository.find_by_id(db, product_id)
    if not product:
        return ProductNotFound()
    return {"product": product}


@router.post("/products", tags=["products"], status_code=status.HTTP_201_CREATED)
async def create_product(product: CreateProductInput, db: Session = Depends(get_db)):
    product_created = product_repository.save(db, product)
    return {"product": product_created}


@router.patch("/products", tags=["products"])
async def update_product(input: UpdateProductInput, db: Session = Depends(get_db)):
    product: Optional[Product] = product_repository.find_by_id(db, input.id)
    if not product:
        return ProductNotFound()

    updated_product = product_repository.update(db, input)
    return {"message": "updated", "product": updated_product}


@router.delete("/products/{product_id}", tags=["products"])
async def delete_product(
    product_id: str,
    db: Session = Depends(get_db)
):
    product: Optional[Product] = product_repository.find_by_id(db, product_id)
    if not product:
        return ProductNotFound()

    product_repository.delete(db, product_id)
    return {"message": "deleted"}
