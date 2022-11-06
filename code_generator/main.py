import os
from typing import List


def generate_main(class_models: List[type]) -> None:
    filename = 'src/main.py'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    open('src/__init__.py', 'a').close()

    with open(filename, 'w+') as f:
        f.write(f"""# -*- coding: utf-8 -*-
from fastapi import FastAPI

from src.infra.models import Base, engine
""")
        models_plural = list(map(lambda model: f'{model.__name__.lower()}s', class_models))
        models_plural_routers = list(map(lambda model: f'router_{model.__name__.lower()}s', class_models))
        f.write(f'from src.application.routers import {", ".join(models_plural_routers)}\n')

        f.write("""
Base.metadata.create_all(bind=engine)

app = FastAPI()
""")

        for model in models_plural:
            f.write(f"app.include_router(router_{model})\n")
