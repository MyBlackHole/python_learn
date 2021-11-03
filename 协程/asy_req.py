import asyncio
import json

import requests


def qingqiu(url):
    return json.loads(requests.get(url).content)


async def hello1(url, n):
    print('55555555555555555555')
    loop = asyncio.get_event_loop()
    reap = await loop.run_in_executor(None, qingqiu, url)
    print('reap', reap, 'n', n)
    print('666666666666')


async def hello(n, url):
    print("协程" + str(n) + "启动")
    await hello1(url, n)
    print("协程" + str(n) + "结束")
    # await hello2(n)


if __name__ == "__main__":
    tasks = []
    _url = 'http://httpbin.org/get'
    for i in range(0, 10):
        tasks.append(hello(i, _url))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
