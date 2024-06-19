# -*- coding: utf-8 -*-
from fastapi import status, HTTPException


class ProductNotFound:
    def __init__(self) -> None:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            [
                {
                    "loc": ["param", "product_id"],
                    "msg": "Product not found",
                    "type": "not_found_error",
                }
            ],
        )
