#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          循环
   Description:
   Author:             Black Hole
   date:               2020/9/2
-------------------------------------------------
   Change Activity:    2020/9/2:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import asyncio

import aiohttp


async def main():
    while True:
        async with aiohttp.ClientSession() as session:
            async with session.get("http://www.baidu.cn/") as response:
                print(response.status)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
