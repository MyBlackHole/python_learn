#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          枚举
   Description:
   Author:             Black Hole
   date:               2020/8/19
-------------------------------------------------
   Change Activity:    2020/8/19:
-------------------------------------------------
"""

__author__ = 'Black Hole'

from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/model/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
