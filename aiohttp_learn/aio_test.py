#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/10/26
# @Author : Twinkle
# @File : aio_test.py
# @Version    : 
# @Description:
import asyncio
import os
import random

import aiofiles
import aiohttp

dir_path = os.path.join(os.getcwd(), "")


async def test():
    url = 'https://p26-dy.byteimg.com/tos-cn-p-0015/85d9f847cf5f4c6995ec535130ecb3cb_1601621736~tplv-dy-360p.jpeg?from=2563711402'
    headers = {
        "User-Agent": "com.ss.android.ugc.aweme.lite/920 (Linux; U; Android 5.1.1; zh_CN; OPPO R11; Build/NMF26X; Cronet/TTNetVersion:4df3ca9d 2019-11-25)",
        'Connection': 'close'
    }
    img_path = os.path.join(dir_path, ''.join(random.choice("0123456789") for i in range(16)) + ".jpeg")
    print(img_path)
    async with aiohttp.ClientSession() as session:
        img_res = await session.get(url, headers=headers)
        # _bytes = await img_res.read()
        # with open(img_path, 'wb') as f:
        #     f.write(_bytes)
        # print(_bytes)
        # _bytes = await img_res.read()

        async with aiofiles.open(img_path, "wb") as f:
            _bytes = await img_res.read()
            await f.write(_bytes)
    print(img_path + " end!")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [test() for i in range(10)]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
