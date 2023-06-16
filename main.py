import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

class EntityItem(BaseModel):
    name: str
    value: str

class Entity(BaseModel):
    items: list[EntityItem]

app = FastAPI()

@app.post("/")
async def build_api(entity: Entity):
    return {"message": "api built"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", reload=True)
