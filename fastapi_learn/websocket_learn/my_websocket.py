#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          my_websocket
   Description:
   Author:             Black Hole
   date:               2020/11/19
-------------------------------------------------
   Change Activity:    2020/11/19:
-------------------------------------------------
"""

__author__ = 'Black Hole'

from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI()


# @app.get("/")
# async def get():
#     return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket):
    await websocket.accept()
    while True:
        # data = await websocket.receive_text()
        await websocket.send_text('2')
        _dict = await websocket.receive_json()
        print(_dict)
        print(websocket.client_state)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, port=8888)
