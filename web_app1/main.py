from enum import Enum
from fastapi import FastAPI

app = FastAPI()

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"


@app.get("/username")
async def root():
    return {"username": "qx"}


@app.get("/nl")
async def nl():
    return {"nl": "18"}


@app.get("/msg/{item_id}")
async def read_item(item_id):
    return {"msg": item_id}


