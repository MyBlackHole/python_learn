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

__author__ = "Black Hole"
from typing import Optional

from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# from fastapi.params import Query

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    username: str
    password: str
    # description: Optional[str] = None
    # price: float
    # tax: Optional[float] = None
    # json1: dict
    # text: Json


# access-control-allow-credentials: true
# access-control-allow-headers: content-type
# access-control-allow-methods: DELETE, GET, HEAD, OPTIONS, PATCH, POST, PUT
# access-control-allow-origin: http://localhost:3002
# access-control-max-age: 600
# content-length: 2
# content-type: text/plain; charset=utf-8
# date: Tue, 25 Jan 2022 01:46:25 GMT
# server: uvicorn
# vary: Origin


# @app.options("/api/user/login")
# def options():
#     headers  = {}
#     headers["access-control-allow-credentials"]= "true"
#     headers["access-control-allow-headers"]= "content-type"
#     headers["access-control-allow-methods"]= "DELETE, GET, HEAD, OPTIONS, PATCH, POST, PUT"
#     headers["access-control-allow-origin"]= "http://localhost:3002"
#     headers["access-control-max-age"]= "600"
#     r  = Response(headers=headers)
#     return r


@app.post("/api/user/login")
def read_item(item: Item, response: Response):
    response.headers["access-control-allow-origin"] = "*"
    return {"code": 200, "msg": None, "data": {"Access-Token": "token_admin_token"}}


# @app.options("/api/user/logout")
# def options():
#     headers  = {}
#     headers["access-control-allow-credentials"]= "true"
#     headers["access-control-allow-headers"]= "*"
#     headers["access-control-allow-methods"]= "DELETE, GET, HEAD, OPTIONS, PATCH, POST, PUT"
#     headers["access-control-allow-origin"]= "http://localhost:3002"
#     headers["access-control-max-age"]= "600"
#     r  = Response(headers=headers)
#     return r


@app.delete("/api/user/logout")
def logout(response: Response):
    response.headers["access-control-allow-credentials"] = "true"
    response.headers["access-control-allow-origin"] = "*"
    # Failed to load resource: net::ERR_FAILED
    return {"code": 200, "msg": None, "data": {"source"}}


@app.get("/api/user/getUser")
def getUser():
    # Failed to load resource: net::ERR_FAILED
    return {"code": 200, "msg": None, "data": {"username": "admin"}}


@app.get("/api/user/getRoute")
def getRoute():
    # Failed to load resource: net::ERR_FAILED
    return {"code": 200, "msg": None, "data": {"username": "admin"}}


@app.get(
    "/api/getProductList",
    description="<a href='https://api.metaengine.yzbtkj.cn/static_file/caption/课程配置阶段结构.html'>kjsdfk </a>",
)
def logout():
    data_list = [
        {
            "name": "string",
            "product_id": "string",
            "data": {
                "a": "a",
                "b": "b",
                "c": "c",
                "d": "d",
            },
        },
        {
            "name": "string",
            "product_id": "string",
            "data": {
                "a": "a",
                "b": "b",
                "c": "c",
            },
        },
    ]
    return {"code": 200, "msg": None, "data": data_list}


# @app.post("/post")
# def post_item(item: Item, item1: Item = Query(default=Item(**{}))):
#     print(item)
#     return item


# @app.put("/items/{item_id}")
# async def create_item(item_id: int, item: Item, q: Optional[str] = None):
#     result = {"item_id": item_id, **item.dict()}
#     if q:
#         result.update({"q": q})
# return result


@app.get("/ok")
def get(a: str):
    return {1: a}


# @app.post("/ok")
# def get():
#     return {1:1}


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

    uvicorn.run(app=app, host="0.0.0.0", port=9999)
    # uvicorn.run(app="app:app", host="0.0.0.0", port=8080, reload=True)
    # uvicorn.run(app="app:app", host="::", port=8080, reload=True)
    # uvicorn.run(app, host="0.0.0.0", port=8010, ssl_keyfile='secret.key', ssl_certfile='secret.pem')
    # import os
    #
    # os.system("uvicorn 1:app --reload")
