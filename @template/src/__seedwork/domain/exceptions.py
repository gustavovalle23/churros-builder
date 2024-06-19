# -*- coding: utf-8 -*-
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
