import asyncio
from pyppeteer import launch
import time


async def main():
    browser = await launch({
        'headless': False,  # 关闭无头模式
        # 'devtools':True, # 打开 chromium 的 devtools
        # 'args': [
        #     '--disable-extensions',
        #     '--hide-scrollbars',
        #     '--disable-bundled-ppapi-flash',
        #     '--mute-audio',
        #     '--no-sandbox',
        #     '--disable-setuid-sandbox',
        #     '--disable-gpu',
        # ],
        # 'dumpio': True,
    })
    page = await browser.newPage()
    await page.goto('http://www.jsbchina.cn/CN/gryw/ptzlc/lc/lccpxx/index.html?flag=1')
    await page.goto('http://www.jsbchina.cn/CN/gryw/ptzlc/lc/lccpxx/index.html?flag=1')

    # await page.goto('http://www.jsbchina.cn/CN/gryw/ptzlc/lc/lccpxx/index.html?flag=1')
    # content = await page.evaluate('document.documentElement', force_expr=True)
    await asyncio.sleep(10)
    # await page.screenshot({'path': 'example.png'})
    # print(page.content())
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
    pages = await browser.pages()
    htmls = []
    for i in pages:
        htmls.append(await i.content())

    for i, html in enumerate(htmls):
        with open(str(i) + '.txt', 'w') as f:
            f.write(html)

    print(browser.targets())
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
