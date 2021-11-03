#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          路径转换器
   Description:
   Author:             Black Hole
   date:               2020/8/19
-------------------------------------------------
   Change Activity:    2020/8/19:
-------------------------------------------------
"""

__author__ = 'Black Hole'

from fastapi import FastAPI

app = FastAPI()


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
