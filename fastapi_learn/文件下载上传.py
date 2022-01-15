#!/usr/bin/env python
# -*- coding: utf-8 -*- 

""" 
------------------------------------------------- 
   File Name:   文件下载上传 
   Description: 
   Author:      Black Hole 
   date:        2021/1/12 

------------------------------------------------- 
   Change Activity: 
                2021/1/12: 
------------------------------------------------- 
"""

__author__ = 'Black Hole'

from typing import List

from fastapi import FastAPI, File, UploadFile
from starlette.responses import FileResponse

app = FastAPI()


@app.get("/file")
def file_dow():
    return FileResponse('./text.zip', filename='test.zip')


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/file/")
async def create_files(file: bytes = File(...)):
    with open('./base.jpg', 'wb') as f:
        f.write(file)

    return {"fileSize": len(file)}


@app.post('/uploadFile')
async def up_load_file(file: UploadFile = File(...)):
    """缺少验证是否上传文件"""
    content = await file.read()
    with open('./test.jpg', 'wb') as f:
        f.write(content)

    return {"filename": file.filename}


@app.post("/files/")
async def create_files(
        files: List[bytes] = File(...)
):
    print(type(files))
    print(files)
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadFiles/")
async def create_upload_files(
        files: List[UploadFile] = File(...)
):
    return {"filenames": [file.filename for file in files]}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
