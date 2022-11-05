import os
import inspect
from typing import Dict, List


def generate_main(class_models: List[type]) -> None:
    filename = 'src/main.py'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    open('src/__init__.py', 'a').close()

    with open(filename, 'w+') as f:
        f.write(f"""# -*- coding: utf-8 -*-
from fastapi import FastAPI

from src.infra.models import Base, engine
""")
        for model in class_models:
            f.write(f"from src.application.routers.{model.__name__.lower()} import router as router_{model.__name__.lower()}s\n")

        f.write("""
Base.metadata.create_all(bind=engine)

app = FastAPI()
""")

        for model in class_models:
            f.write(f"app.include_router(router_{model.__name__.lower()}s)\n")
