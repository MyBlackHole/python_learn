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

from fastapi import FastAPI

app = FastAPI()


@app.get("/ping")
def read_item():
    return {"user": "black", "value": "hole"}



if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="main:app", host="0.0.0.0", port=8090)
