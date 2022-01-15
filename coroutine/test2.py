import asyncio


async def fu(wait, str1):
    await asyncio.sleep(10)
    print(str1)


async def main():
    print('start')
    # await fu(1, '1')
    # await fu(2, '2')
    task1 = asyncio.create_task(fu(1, '1'))
    task1 = asyncio.create_task(fu(2, '2'))
    print('end')


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
