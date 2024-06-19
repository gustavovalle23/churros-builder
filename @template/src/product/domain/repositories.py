
# -*- coding: utf-8 -*-
from typing import Tuple
from abc import ABCMeta, abstractmethod

from src.product.domain.entities import Product


class ProductRepository(metaclass=ABCMeta):
    @abstractmethod
    def find_all(self) -> Tuple[Product]:
        """
        Method responsable for find all products considering pagination
        """
        pass

    @abstractmethod
    def find_by_id(self, product_id: int) -> Product | None:
        """
        Method responsable for find product by id
        """
        pass

    @abstractmethod
    def save(self, input_save_product) -> Product:
        """
        Method responsable for save product
        """
        pass

    @abstractmethod
    def update(self, input_update_product) -> Product:
        """
        Method responsable for update product
        """
        pass

    @abstractmethod
    def inactivate(self, product_id: int) -> None:
        """
        Method responsable for inactive product
        """
        pass

    @abstractmethod
    def delete(self, product_id: int) -> None:
        """
        Method responsable for delete product
        """
        pass
