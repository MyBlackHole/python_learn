#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          数值校验
   Description:
   Author:             Black Hole
   date:               2020/8/19
-------------------------------------------------
   Change Activity:    2020/8/19:
-------------------------------------------------
"""

__author__ = "Black Hole"

from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    *,
    item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000),
    q: str,
    size: float = Query(..., gt=0, lt=10.5)
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
