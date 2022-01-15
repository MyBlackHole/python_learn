#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
File Name:   异常接管
Description:
Author:      Black Hole
date:        2021/08/10 10:43:25:

-------------------------------------------------
Change Activity:
			 2021/08/10 10:43:25:
-------------------------------------------------
"""


from pydantic import BaseModel
from typing import Optional
from fastapi.exceptions import HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from fastapi import FastAPI
from fastapi.exception_handlers import request_validation_exception_handler, http_exception_handler


app = FastAPI()


@app.exception_handler(HTTPException)  # 自定义HttpRequest 请求异常
async def http_exception_handle(request, exc):
    """
	改写默认的HttpException
    :param request: 请求必不可少
    :param exc: 错误栈处理
    :return:
    """
    return http_exception_handler(request=request, exc=exc)

# @app.exception_handler(RequestValidationError)
# async def request_validatoion_error(request, exc):
#     """
#     重写 request 错误
#     :param request: 必填项
#     :param exc: 错误信息栈
#     :return:
#     """
#     return PlainTextResponse(str(exc), status_code=exc.json())

"""自定义RequestValidationError 重写请求验证异常"""


@app.exception_handler(RequestValidationError)
async def request_validatoion_error(request, exc):
    """
	重写 request 错误
    :param request: 必填项
    :param exc: 错误信息栈
    :return:
    """
    return request_validation_exception_handler(request=request, exc=exc)


@app.get("/", status_code=202)
def get():
    raise HTTPException(status_code=400, detail={
                        "status": 0, "msg": "参数缺失", "data": ""})

# 默认HttpException 错误异常


@app.get('/http_exception')
async def http_exception(city: str):
    if city != 'BeiJing':
        raise HTTPException(
            status_code=404, detail='city not found', headers={'x_token': 'xxx'})
    return {'message': 'no city'}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


class Item(BaseModel):
    name: str


@app.post("/item")
def post_item(item: Item):
	if item.name == "1":
        raise HTTPException(
            status_code=404, detail='city not found', headers={'x_token': 'xxx'})
    return item


if __name__ == "__main__":
    # Thread(target=func).start()
    import uvicorn

    uvicorn.run(app=app, host="0.0.0.0", port=8080)
    # uvicorn.run(app="app:app", host="0.0.0.0", port=8080, workers=4)
    # uvicorn.run(app, host="0.0.0.0", port=8010, ssl_keyfile='/home/black/Documents/Code/Python/python_learn/fastapi_learn/secret.key', ssl_certfile='/home/black/Documents/Code/Python/python_learn/fastapi_learn/secret.pem')
    # import os
    #
    # os.system("uvicorn 1:app --reload")
