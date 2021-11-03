#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio

import aiohttp
from retrying import retry


async def aio_get(url: str, **kwargs: dict):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, timeout=10, **kwargs) as response:
            assert response.status == 200
            return await response.read()


async def fetch(session, url):
    async with session.get(url, timeout=10) as response:
        return await response.read()


async def main():
    while True:
        with aiohttp.ClientSession() as session:
            text = await fetch(session, "https://www.baidu.com/")
            return text


async def run():
    try:
        text = await main()
        print(text)
    except Exception as e:
        raise Exception(e)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(aio_get(url='http://www.baidu.com/'))

    # loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(loop)
    # task = asyncio.ensure_future(aio_get(url='http://www.baidu.com/'))
    # resp = loop.run_until_complete(asyncio.wait([task]))
    # print(resp)
