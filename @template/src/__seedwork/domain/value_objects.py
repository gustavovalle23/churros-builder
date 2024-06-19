# -*- coding: utf-8 -*-
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
