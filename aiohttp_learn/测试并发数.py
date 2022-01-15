#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          测试并发数
   Description:
   Author:             Black Hole
   date:               2020/10/12
-------------------------------------------------
   Change Activity:    2020/10/12:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import asyncio

import aiohttp
from loguru import logger


# 定义异步函数
async def fetch(url):
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        # async with session.get(url) as response:
        #     text = await response.read()
        #     logger.info(text)
        response = await session.get(url)
        text = await response.read()
        return text
        # logger.info(text)


async def request_url(url):
    resp_dict = {}
    try:
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            resp = await session.get(url)
            if resp.status == 200:
                real_url = str(resp.real_url)
                text = await resp.text(errors='ignore')
                resp_dict = {
                    'text': text,
                    'status': resp.status,
                    'real_url': real_url,
                    'cookie': resp.cookies
                }
            else:
                logger.error(f'访问{url}失败,状态码{resp.status}')

        # logger.info(resp_dict)
    except Exception as e:
        logger.error(f'访问{url.encode("utf-8", "ignore").decode("utf-8", "ignore")},原因：{e}')
    return resp_dict


def run(num: int, url: str):
    main_loop = asyncio.get_event_loop()
    # main_loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(main_loop)
    task_list = []
    for i in range(num):
        task = asyncio.ensure_future(request_url(url), loop=main_loop)
        # task = asyncio.ensure_future(fetch(url), loop=main_loop)
        task_list.append(task)

    data_list = main_loop.run_until_complete(asyncio.wait(task_list))
    # data_list = main_loop.run_until_complete(asyncio.gather(*task_list))
    print(data_list)
    print(len(data_list))


if __name__ == '__main__':
    # url_test = 'http://dispatch.yunrunyuqing.com:38082/ScheduleDispatch/dispatch?type=3'
    url_test = 'https://m.weibo.cn/api/container/getIndex?from[]=feed&from[]=feed&loc[]=nickname&loc[]=nickname&loc[]=nickname&is_all[]=1%3Ffrom%3Dfeed&is_all[]=1&is_all[]=1&jumpfrom=weibocom&type=uid&value=5615627418&containerid=1076035615627418&since_id=4580717352725030'
    run(500, url=url_test)
