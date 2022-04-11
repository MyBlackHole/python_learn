import asyncio
from pyppeteer import launch
# from pyppeteer.page import Page


async def main():
    browser = await launch({
        'headless': False,  # 关闭无头模式
        'devtools': True,  # 打开 chromium 的 devtools
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
    await asyncio.sleep(6)
    page = await browser.newPage()
    await page.goto('https://hk.sz.gov.cn:8118')

    # await page.click()

    # # 获取标题
    # title = await page.title()

    # # 获取所有 pages
    # page_list = await browser.pages()

    # # 设置登陆cookie
    # login_cookie= {
    #     'name': 'e9f8e068664b439699445dd42d22de12',
    #     'value': 'wvxIIrZxeuXtKk9xlpd3IeP9bvfMMB+9ZUsDKb2gYEqR0/6xzd6f9Mt5ZQEGyHXcTvD+oo7T+k+N8GlemuBC5S+Pkx8Q3SFTC8TFDvMzaznDLK3GNhgvfdjFI5vzevfOIFk2zLq6M6TV/47BWfsVQg==',
    #     'domain': 'hk.sz.gov.cn',
    #     'path': '/',
    #     # 'expires': 1649589652.063307,
    #     # 'size': 58,
    #     'httpOnly': True,
    #     'secure': True,
    #     'session': False,
    #     'sameSite': 'Lax'
    # }
    # await page.setCookie(login_cookie)

    # # # 个人页
    # # await page.goto('https://hk.sz.gov.cn:8118/userPage/userCenter')

    # # 预约页
    # await page.goto('https://hk.sz.gov.cn:8118/passInfo/detail')

    # await page.screenshot({'path': 'example.png'})
    #
    # dimensions = await page.evaluate('''() => {
    #     return {
    #         width: document.documentElement.clientWidth,
    #         height: document.documentElement.clientHeight,
    #         deviceScaleFactor: window.devicePixelRatio,
    #     }
    # }''')

    # print(dimensions)
    # >>> {'width': 800, 'height': 600, 'deviceScaleFactor': 1}
    cookies = await page.cookies()
    print(cookies)
    await asyncio.sleep(800)
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
