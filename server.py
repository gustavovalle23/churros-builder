import uvicorn
from fastapi import FastAPI

from code_generator.domain.entities import generate_entity, EntityItem
from code_generator.seedwork.domain import generate_domain_seedwork
from code_generator.seedwork.application import generate_use_cases
from code_generator.domain.repositories import generate_repository
from code_generator.infra.models import generate_model
from code_generator.infra.repositories import generate_repository
from code_generator.application import generate_routers
from code_generator.main import generate_main

items = [EntityItem(name='name', type='str', default_value='Gus')]
generate_entity('user', items)
generate_domain_seedwork()
generate_use_cases()
generate_repository('user', items)
generate_model('user', items)

# app = FastAPI()

# @app.post("/")
# async def build_api(entity: Entity):
#     return {"message": "api built"}

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", reload=True)
