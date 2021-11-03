import asyncio
import re

import aiohttp
from requests_html import HTMLSession

n = 1
session = HTMLSession()
r = session.get('https://music.163.com/discover/toplist?id=3779629')
id = re.findall(r'/song\?id=(\d+)"', r.text)
name = re.findall(r'song\?id=\d+">([\w ().&\'（）\[\]，]+)</a>', r.text)


async def get_request(session, url, i):
    print("get_request")
    j = re.sub(r'\(\).&\'（）\[\]，', '', name[i])
    async with session.get(url) as response:
        async with open("mp3/" + str(j) + ".mp3", 'wb') as w:
            for line in response.content:
                await w.write(line)
        print(str(j) + '下载成功')
        # return response


async def save_mp3(i):
    print("save_mp3")
    async with aiohttp.ClientSession() as session:
        await get_request(session, "http://music.163.com/song/media/outer/url?id=" + str(id[i]) + ".mp3", i)


async def main(i):
    print(i)
    await save_mp3(i)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = []
    for i in range(100):
        tasks.append(asyncio.ensure_future(main(i)))
    loop.run_until_complete(asyncio.wait(tasks))
