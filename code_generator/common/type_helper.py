from enum import Enum


class CustomEnum(Enum):
    def __eq__(self, other):
        if isinstance(other, int):
            return self.value == other
        return super().__eq__(other)
