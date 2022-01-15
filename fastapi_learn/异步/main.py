#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          异步
   Description:
   Author:             Black Hole
   date:               2020/7/23
-------------------------------------------------
   Change Activity:    2020/7/23:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import users
import uvicorn
from fastapi import FastAPI

app = FastAPI()
@app.get('/')
async def get():
    return {'msg': 'black hole'}

@app.get('/my_time')
async def my_time():
    time.sleep(10)
    return {'msg': 'my_time'}

if __name__ == "__main__":
    uvicorn.run(app)
