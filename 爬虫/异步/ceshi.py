import asyncio

import aiohttp


async def fetch(session, url):
    print(123)
    async with session.get(url) as response:
        return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'http://python.org')
        print(html)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = []
    for i in range(100):
        tasks.append(asyncio.ensure_future(main()))
    loop.run_until_complete(asyncio.wait(tasks))
