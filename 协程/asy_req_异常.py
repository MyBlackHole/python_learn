import asyncio

import requests


@asyncio.coroutine
def hello1(url):
    yield print('55555555555555555555')
    print('是否执行请求')
    resp = requests.get(url)
    print('666666666666')


async def hello(n, url):
    print("协程" + str(n) + "启动")
    await hello1(url)
    print("协程" + str(n) + "结束")


if __name__ == "__main__":
    tasks = []
    _url = 'https://www.baidu.com/'
    for i in range(0, 10):
        tasks.append(hello(i, _url))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
