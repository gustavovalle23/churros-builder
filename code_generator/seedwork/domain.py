import os


def generate_entities() -> None:
    filename = 'src/__seedwork/domain/entities.py'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    open('src/__seedwork/domain/__init__.py', 'a').close()

    with open(filename, 'w+') as f:
        f.write("""# -*- coding: utf-8 -*-
from abc import ABC
from typing import Any
from dataclasses import Field, dataclass, field, asdict

from src.__seedwork.domain.value_objects import UniqueEntityId


@dataclass(frozen=True, slots=True)
class Entity(ABC):

    unique_entity_id: UniqueEntityId = field(
        default_factory=lambda: UniqueEntityId()
    )

    @property
    def id(self):
        return str(self.unique_entity_id)

    def _set(self, name: str, value: Any):
        object.__setattr__(self, name, value)
        return self

    def to_dict(self):
        entity_dict = asdict(self)
        entity_dict.pop('unique_entity_id')
        entity_dict['id'] = self.id
        return entity_dict

    @classmethod
    def get_field(cls, entity_field: str) -> Field:
        return cls.__dataclass_fields__[entity_field]


""")


def generate_exceptions():
    filename = 'src/__seedwork/domain/exceptions.py'
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, 'w+') as f:
        f.write("""# -*- coding: utf-8 -*-
class ValidationException(Exception):
    pass


class EntityValidationException(Exception):
    from src.__seedwork.domain.validators import ErrorFields

    error: ErrorFields

    def __init__(self, error: ErrorFields) -> None:
        self.error = error
        super().__init__('Entity Validation Error')


class NotFoundException(Exception):
    pass
""")


def generate_repositories():
    filename = 'src/__seedwork/domain/repositories.py'
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, 'w+') as f:
        f.write("""# -*- coding: utf-8 -*-
import abc
from abc import ABC
from typing import Generic, List, TypeVar

from src.__seedwork.domain.entities import Entity
from src.__seedwork.domain.value_objects import UniqueEntityId

ET = TypeVar('ET', bound=Entity)


class RepositoryInterface(Generic[ET], ABC):

    @abc.abstractmethod
    def insert(self, entity: ET) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def find_by_id(self, entity_id: str | UniqueEntityId) -> ET:
        raise NotImplementedError()

    @abc.abstractmethod
    def find_all(self) -> List[ET]:
        raise NotImplementedError()

    @abc.abstractmethod
    def update(self, entity: ET) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self, entity_id: str | UniqueEntityId) -> None:
        raise NotImplementedError()
""")    


def generate_validators():
    filename = 'src/__seedwork/domain/validators.py'
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, 'w+') as f:
        f.write("""# -*- coding: utf-8 -*-
import abc
from abc import ABC
from dataclasses import dataclass
from typing import Any, Dict, Generic, List, TypeVar

from src.__seedwork.domain.exceptions import ValidationException


@dataclass(frozen=True, slots=True)
class ValidatorRules:
    value: Any
    prop: str

    @staticmethod
    def values(value: Any, prop: str):
        return ValidatorRules(value, prop)

    def required(self) -> 'ValidatorRules':
        if self.value is None or self.value == '':
            raise ValidationException(f'The {self.prop} is required')
        return self

    def string(self) -> 'ValidatorRules':
        if self.value is not None and not isinstance(self.value, str):
            raise ValidationException(f'The {self.prop} must be a string')
        return self

    def max_length(self, max_length: int) -> 'ValidatorRules':
        if self.value is not None and len(self.value) > max_length:
            raise ValidationException(
                f'The {self.prop} must be less than {max_length} characters')
        return self

    def boolean(self) -> 'ValidatorRules':
        if self.value is not None and self.value is not True and self.value is not False:
            raise ValidationException(f'The {self.prop} must be a boolean')
        return self


ErrorFields = Dict[str, List[str]]

PropsValidated = TypeVar('PropsValidated')


@dataclass(slots=True)
class ValidatorFieldsInterface(ABC, Generic[PropsValidated]):
    errors: ErrorFields = None
    validated_data: PropsValidated = None

    @abc.abstractmethod
    def validate(self, data: Any) -> bool:
        raise NotImplementedError()
""")    


def generate_value_objects():
    filename = 'src/__seedwork/domain/value_objects.py'
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, 'w+') as f:
        f.write("""# -*- coding: utf-8 -*-
import json
from abc import ABC
from dataclasses import dataclass, field, fields


@dataclass(frozen=True, slots=True)
class ValueObject(ABC):

    def __str__(self) -> str:
        fields_name = [field.name for field in fields(self)]
        if len(fields_name) == 1:
            return str(getattr(self, fields_name[0]))
        return json.dumps({
                field_name: getattr(self, field_name) 
                for field_name in fields_name
            })
""")    




def generate_domain_seedwork() -> None:
    generate_entities()
    generate_exceptions()
    generate_repositories()
    generate_validators()
    generate_value_objects()
