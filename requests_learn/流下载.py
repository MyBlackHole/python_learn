#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          流下载
   Description:
   Author:             Black Hole
   date:               2020/9/9
-------------------------------------------------
   Change Activity:    2020/9/9:
-------------------------------------------------
"""

__author__ = "Black Hole"

import requests

if __name__ == "__main__":
    headers = {}
    url = "https://txmov2.a.yximgs.com/bs2/newWatermark/Mzg0NjQ5MzA1Mjg_zh_15.mp4"
    response = requests.get(url, headers=headers, stream=True, verify=False)
    size = 0
    chunk_size = 1042
    with open("Mzg0NjQ5MzA1Mjg_zh_15.mp4", "wb") as file:
        for data in response.iter_content(chunk_size=chunk_size):
            file.write(data)
            size += len(data)
            file.flush()
            print(f"{size}")
            if size > 1024 * 1024 * 100:
                break
    print(f"下载完成")
