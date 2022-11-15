import asyncio
from pyppeteer import launch


async def main():
    browser = await launch({
        'headless': False,  # 关闭无头模式
        # 'devtools': True,  # 打开 chromium 的 devtools
        'args': [
            '--disable-extensions',
            '--hide-scrollbars',
            '--disable-bundled-ppapi-flash',
            '--mute-audio',
            '--no-sandbox',
            '--disable-setuid-sandbox',
            '--disable-gpu',
        ],
        'dumpio': True,
    })
    page = await browser.newPage()
    await page.goto(
        'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&hs=0&xthttps=111110&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%B0%8F%E5%A7%90%E5%A7%90&oq=%E5%B0%8F%E5%A7%90%E5%A7%90&rsp=-1')
    # await page.goto('http://www.jsbchina.cn/CN/gryw/ptzlc/lc/lccpxx/index.html?flag=1')

    # await page.goto('http://www.jsbchina.cn/CN/gryw/ptzlc/lc/lccpxx/index.html?flag=1')
    # content = await page.evaluate('document.documentElement', force_expr=True)
    for i in range(100):
        await page.evaluate('_ => {window.scrollBy(0, window.innerHeight);}')  
        await asyncio.sleep(1)

    # await asyncio.sleep(10)
    # await page.screenshot({'path': 'example.png'})
    html = await page.content()
    # print(html)
    with open('image.baidu.com.txt', 'w') as f:
        f.write(html)
    print("ok")
    # content = await page.evaluate('document.body.textContent', force_expr=True)
    # dimensions = await page.evaluate('''() => {
    #     return {
    #         test: window
    #     }
    # }''')

    # print(content)
    # print(dimensions['document'])
    # print(dimensions['test'])
    # with open('jiangshu.html', 'w') as f:
    #     f.write()
    # >>> {'width': 800, 'height': 600, 'deviceScaleFactor': 1}
    # pages = await browser.pages()
    # htmls = []
    # for i in pages:
    #     htmls.append(await i.content())

    # for i, html in enumerate(htmls):
    #     with open(str(i) + '.txt', 'w') as f:
    #         f.write(html)

    # print(browser.targets())
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
