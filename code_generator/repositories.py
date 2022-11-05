import os
import inspect
from typing import Dict

from code_generator.common.templates import *


def generate_repository(class_model: type) -> None:
    filename = f'src/infra/repositories/{class_model.__name__.lower()}.py'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    open('src/infra/repositories/__init__.py', 'a').close()

    model_name = f'{class_model.__name__.capitalize()}'

    attributes: Dict[str, type] = inspect.getmembers(class_model())[0][1]
    with open(filename, 'w+') as f:
        f.write(imports_repository)

        f.write(f"""
from src.domain.entities.{class_model.__name__.lower()} import {model_name}
from src.infra.models import {model_name}Model
""")


        f.write(f"""
def to_entity(model: Query | {model_name}Model) -> {model_name} | None:
    if not model:
        return

    return {model_name}(\n""")

        for field, type_of_field in attributes.items():
            f.write(f"""        model.{field},\n""")
        f.write("""    )""")
            
#             if type_of_field.__module__ == "builtins":
#                 continue
#             f.write(
#                 f'from {type_of_field.__module__} import {type_of_field.__name__}\n')

#         f.write(f"""\n\n@dataclass(frozen=True)
# class {class_model.__name__.capitalize()}:
#     id: uuid""")

#         for field, type_of_field in attributes.items():
#             if field == "id":
#                 continue

#             f.write(
#                 f"""
#     {field}: {type_of_field.__name__}""")
#         f.write("\n")

