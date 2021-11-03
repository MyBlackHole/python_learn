#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          1
   Description:
   Author:             Black Hole
   date:               2020/7/22
-------------------------------------------------
   Change Activity:    2020/7/22:
-------------------------------------------------
"""

__author__ = 'Black Hole'
from typing import Optional

from contextlib import contextmanager
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.params import Query

app = FastAPI()


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


class Item(BaseModel):
    name: str
    # description: Optional[str] = None
    # price: float
    # tax: Optional[float] = None
    # json1: dict
    # text: Json


@app.post("/post")
def post_item(item: Item, item1: Item = Query(default=Item(**{}))):
    print(item)
    return item


@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: Optional[str] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result


@app.get("/ok")
def get(a: str):
    return {1:a}


@app.post("/ok")
def get():
    return {1:1}


# @app.middleware('http')
# async def tokenCheck(request: Request, call_next):
#
#     if '/ok' in request.url.path or '/post' in request.url.path:
#         query_string = request.scope['query_string']
#         ok = request.query_params['a']
#         request.body().decode()
#         b = "123213"
#         request.scope['query_string'] = query_string.replace(ok.encode(), b.encode())
#
#     response = await call_next(request)
#     return response

if __name__ == "__main__":
    # Thread(target=func).start()
    import uvicorn

    uvicorn.run(app="app:app", host="0.0.0.0", port=8080)
    # uvicorn.run(app, host="0.0.0.0", port=8010, ssl_keyfile='/home/black/Documents/Code/Python/python_learn/fastapi_learn/secret.key', ssl_certfile='/home/black/Documents/Code/Python/python_learn/fastapi_learn/secret.pem')
    # import os
    #
    # os.system("uvicorn 1:app --reload")
