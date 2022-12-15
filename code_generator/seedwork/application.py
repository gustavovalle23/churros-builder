# -*- coding: utf-8 -*-
import os


def generate_use_cases() -> None:
    filename = 'src/__seedwork/application/use_cases.py'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    open('src/__seedwork/application/__init__.py', 'a').close()

    with open(filename, 'w+') as f:
        f.write("""# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Any

Input = TypeVar("Input")
Output = TypeVar("Output")


class UseCase(Generic[Input, Output], ABC):
    @abstractmethod
    def execute(self, input_use_case: Input, db: Any) -> Output:
        raise NotImplementedError()
""")
