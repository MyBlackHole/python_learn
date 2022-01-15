import asyncio
from pyppeteer import launch


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
    page = await browser.newPage()
    await page.goto('http://www.jsbchina.cn/CN/gryw/ptzlc/lc/lccpxx/index.html?flag=1')
    # await page.goto(
    #     'https://www.southwest.com/air/booking/select.html?adultPassengersCount=1&departureDate=2020-04-30&departureTimeOfDay=ALL_DAY&destinationAirportCode=BDL&fareType=USD&int=HOMEQBOMAIR&originationAirportCode=LAX&passengerType=ADULT&reset=true&returnDate=2020-05-01&returnTimeOfDay=ALL_DAY&seniorPassengersCount=0&tripType=roundtrip')

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
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
