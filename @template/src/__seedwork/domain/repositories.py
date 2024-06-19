# -*- coding: utf-8 -*-
import abc
from abc import ABC
from typing import Generic, List, TypeVar

from src.__seedwork.domain.entities import Entity

ET = TypeVar('ET', bound=Entity)


class RepositoryInterface(Generic[ET], ABC):

    @abc.abstractmethod
    def insert(self, entity: ET) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def find_by_id(self, entity_id: str) -> ET:
        raise NotImplementedError()

    @abc.abstractmethod
    def find_all(self) -> List[ET]:
        raise NotImplementedError()

    @abc.abstractmethod
    def update(self, entity: ET) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self, entity_id: str) -> None:
        raise NotImplementedError()
