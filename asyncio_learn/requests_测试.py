#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          requests_测试
   Description:
   Author:             Black Hole
   date:               2020/9/21
-------------------------------------------------
   Change Activity:    2020/9/21:
-------------------------------------------------
"""

__author__ = "Black Hole"

import asyncio

import aiohttp
import requests


async def func(url, i):
    print(i)
    return requests.get(url=url)


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def func1(url, i):
    print(i)
    async with aiohttp.ClientSession() as session:
        return await fetch(session, url)


tasks = []
main_loop = asyncio.new_event_loop()
asyncio.set_event_loop(main_loop)
for i in range(10):
    task = asyncio.ensure_future(func1(r"http://www.google.com/", i), loop=main_loop)
    tasks.append(task)
main_loop.run_until_complete(asyncio.wait(tasks))
main_loop.close()
