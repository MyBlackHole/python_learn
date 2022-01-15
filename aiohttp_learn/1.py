#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio

import aiohttp

headers = {
    "Content-Type": "application/json; charset=UTF-8"
}

async def aio_get(url: str, **kwargs: dict):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, timeout=10, **kwargs) as response:
            assert response.status == 200
            return await response.read()


async def aio_post(url: str, **kwargs: dict):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, timeout=10, **kwargs) as response:
            assert response.status == 200
            ret = await response.json()
            print(ret)
            return ret 

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
    _json = {
        "msg": "我是谁"
    }
    loop.run_until_complete(aio_post(url='http://httpbin.org/post', data=_json))
    loop.run_until_complete(aio_post(url='http://httpbin.org/post?a=1', data=_json))
    loop.run_until_complete(aio_post(url='http://httpbin.org/post', data=_json, headers=headers))
    loop.run_until_complete(aio_post(url='http://httpbin.org/post', json=_json))
    # loop.run_until_complete(aio_get(url='http://www.baidu.com/'))

    # loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(loop)
    # task = asyncio.ensure_future(aio_get(url='http://www.baidu.com/'))
    # resp = loop.run_until_complete(asyncio.wait([task]))
    # print(resp)
