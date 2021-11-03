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

from . import users
import uvicorn
from fastapi import FastAPI

app = FastAPI()
app.include_router(users.router, prefix='/users', tags=['users'])

if __name__ == "__main__":
    uvicorn.run(app)
