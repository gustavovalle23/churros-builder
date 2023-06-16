import os

def generate_entity_file(entity_name, fields):
    content = f"""from pydantic import BaseModel

class {entity_name}Base(BaseModel):
    id: str
    name: str
    age: int

class {entity_name}Create({entity_name}Base):
    pass

class {entity_name}({entity_name}Base):
    class Config:
        orm_mode = True
"""
    with open(f"{entity_name.lower()}.py", "w") as file:
        file.write(content)

def generate_router_file(entity_name):
    content = f"""from fastapi import APIRouter, Depends
from typing import List
from . import {entity_name.lower()}_service, {entity_name.lower()}_schemas

router = APIRouter()

@router.get("/", response_model=List[{entity_name.lower()}_schemas.{entity_name}])
def get_{entity_name.lower()}s():
    return {entity_name.lower()}_service.get_{entity_name.lower()}s()

@router.post("/", response_model={entity_name.lower()}_schemas.{entity_name})
def create_{entity_name.lower()}({entity_name.lower()}: {entity_name.lower()}_schemas.{entity_name}Create):
    return {entity_name.lower()}_service.create_{entity_name.lower()}({entity_name.lower()})

@router.get("/{entity_name.lower()}_id", response_model={entity_name.lower()}_schemas.{entity_name})
def get_{entity_name.lower()}({entity_name.lower()}_id: str):
    return {entity_name.lower()}_service.get_{entity_name.lower()}({entity_name.lower()}_id)

@router.put("/{entity_name.lower()}_id", response_model={entity_name.lower()}_schemas.{entity_name})
def update_{entity_name.lower()}({entity_name.lower()}_id: str, {entity_name.lower()}: {entity_name.lower()}_schemas.{entity_name}):
    return {entity_name.lower()}_service.update_{entity_name.lower()}({entity_name.lower()}_id, {entity_name.lower()})

@router.delete("/{entity_name.lower()}_id")
def delete_{entity_name.lower()}({entity_name.lower()}_id: str):
    return {entity_name.lower()}_service.delete_{entity_name.lower()}({entity_name.lower()}_id)
"""
    with open(f"{entity_name.lower()}_router.py", "w") as file:
        file.write(content)

def generate_service_file(entity_name):
    content = f"""from typing import List
from . import {entity_name.lower()}_schemas

def get_{entity_name.lower()}s():
    # Implement your logic here to get a list of {entity_name} objects from the database
    # For now, returning a dummy list
    return []

def create_{entity_name.lower()}({entity_name.lower()}: {entity_name.lower()}_schemas.{entity_name}Create):
    # Implement your logic here to create a new {entity_name} object in the database
    # For now, returning the input object
    return {entity_name.lower()}

def get_{entity_name.lower()}({entity_name.lower()}_id: str):
    # Implement your logic here to get a single {entity_name} object from the database
    # For now, returning a dummy object
    return {entity_name.lower()}_schemas.{entity_name}(id={entity_name.lower()}_id, name="John", age=30)

def update_{entity_name.lower()}({entity_name.lower()}_id: str, {entity_name.lower()}: {entity_name.lower()}_schemas.{entity_name}):
    # Implement your logic here to update a {entity_name} object in the database
    # For now, returning the updated object
    return {entity_name.lower()}

def delete_{entity_name.lower()}({entity_name.lower()}_id: str):
    # Implement your logic here to delete a {entity_name} object from the database
    # For now, returning True to indicate success
    return True
"""
    with open(f"{entity_name.lower()}_service.py", "w") as file:
        file.write(content)

def generate_schema_file(entity_name):
    content = f"""from pydantic import BaseModel

class {entity_name}(BaseModel):
    id: str
    name: str
    age: int
"""
    with open(f"{entity_name.lower()}_schemas.py", "w") as file:
        file.write(content)

def generate_api_files(data):
    entity_name = data['entity_name']
    os.makedirs(entity_name.lower(), exist_ok=True)
    os.chdir(entity_name.lower())

    generate_entity_file(entity_name, data)
    generate_router_file(entity_name)
    generate_service_file(entity_name)
    generate_schema_file(entity_name)

    os.chdir("..")

# Example usage:
data = {'entity_name': 'User', 'id': 'string', 'name': 'string', 'age': 'int'}
generate_api_files(data)
