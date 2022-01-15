#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/15
# @Author : Twinkle
# @File : 给事件循环添加协程对象.py
# @Version    : 
# @Description:
import asyncio
import json
import queue
from threading import Thread

import aiohttp
import pymysql
from loguru import logger

myqueue = queue.Queue(maxsize=10)
myqueue.put(9617619)
semaphore = asyncio.Semaphore(5)


def save_to_mysql(items_list):
    connect, cursor = None, None
    logger.info('---这里开始入库---')
    try:
        connect = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='',
            db='bilibili',
            charset='utf8mb4',
        )
        connect.ping()
        cursor = connect.cursor()
        for item in items_list:
            cols, values = zip(*item.items())
            sql = 'INSERT INTO bili_user({}) values({}) ON DUPLICATE KEY UPDATE {};'.format(
                ','.join(cols),
                ','.join(['%s'] * len(values)),
                ','.join(['`{}`=%s'.format(k) for k in cols])
            )
            cursor.execute(sql, values * 2)
        connect.commit()
    except Exception as e:
        logger.info('数据入库出现的错误：%s' % e)
    finally:
        if connect:
            connect.close()


async def forEachUser(user_id, i):
    headers = {
        'authority': 'api.bilibili.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'accept': '*/*',
        'referer': 'https://space.bilibili.com/',
        'accept-language': 'zh-CN,zh;q=0.9',
    }
    url = f'https://api.bilibili.com/x/relation/followings?vmid={user_id}&pn={i}&ps=20&order=desc&jsonp=jsonp&callback=__jp{i + 2}'
    async with semaphore:
        async with aiohttp.ClientSession() as ssesion:
            async with ssesion.get(url, headers=headers) as response:
                result_text = await response.text()
    result = []
    try:
        datalist = json.loads(result_text[6:-1]).get("data").get("list")
        if datalist:
            for x in datalist:
                result.append({
                    "uname": str(x["uname"]),
                    "mid": int(x["mid"]),
                    "face": x["face"],
                })
                myqueue.put(x["mid"])
        logger.info(f"用户id：{user_id},第{i}页数据：{result}")
        save_to_mysql(result)
    except Exception as e:
        logger.info(f"异常：用户id：{user_id}的第{i}页数据：{result_text}={e}")


def production_task():
    while True:
        user_id = myqueue.get()
        if user_id:
            for i in range(1, 6):
                asyncio.run_coroutine_threadsafe(forEachUser(user_id, i), loop)


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    run_loop_thread = Thread(target=production_task)
    run_loop_thread.start()
    loop.run_forever()
