#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          多路径和查询参数
   Description:
   Author:             Black Hole
   date:               2020/8/19
-------------------------------------------------
   Change Activity:    2020/8/19:
-------------------------------------------------
"""

__author__ = 'Black Hole'

from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/users/{user_id}")
async def read_user_item(
        user_id: int, item_id: Optional[int] = 0, q: Optional[str] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
