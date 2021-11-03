# *****************************************
# asyncio.run()

# # 一
# import asyncio
#
#
# async def main():
#     print("hello")
#     await asyncio.sleep(1)
#     print("world")
#
#
# asyncio.run(main())

# # 二
# import asyncio
# import time
#
#
# async def fu(wait, str):
#     await asyncio.sleep(wait)
#     print(str)
#
#
# async def main():
#     print("开始")
#     await fu(4, "一")
#     await fu(1, "二")
#     print("结束")
#
#
# asyncio.run(main())

# *****************************************

# asyncio.create_task

# # 一
# import asyncio
# import time
#
#
# async def fu(wait, str):
#     await asyncio.sleep(wait)
#     print(str)
#
#
# async def main():
#     # 创建并发协程
#     task1 = asyncio.create_task(fu(2, '一'))
#     task2 = asyncio.create_task(fu(1, '二'))
#     print(f"start {time.strftime('%X')}")
#     await task1
#     await task2
#     print(f"end {time.strftime('%X')}")
#
#
# asyncio.run(main())
# *****************************************

# asyncio.sleep

# # 一
# import asyncio
# import datetime
#
#
# async def display_date():
#     loop = asyncio.get_running_loop()
#     end_time = loop.time() + 5
#     while True:
#         print(datetime.datetime.now())
#         if (loop.time() + 1.0) >= end_time:
#             break
#         await asyncio.sleep(1)
#
#
# asyncio.run(display_date())

# *****************************************
# asyncio.gather

# # 一
# import asyncio
#
#
# async def factorial(name, number):
#     f = 1
#     for i in range(2, number + 1):
#         assert f > 4
#         print(f"task {name}:{i}")
#         await asyncio.sleep(1)
#         f *= i
#     print(f"task {name}:{f}")
#
#
# async def factorial1(name, number):
#     f = 1
#     for i in range(2, number + 1):
#         print(f"task {name}:{i}")
#         await asyncio.sleep(1)
#         f *= i
#     print(f"task {name}:{f}")
#
#
# async def main():
#     await asyncio.gather(
#         factorial("A", 2),
#         factorial1("B", 3),
#         factorial1("C", 4),
#         return_exceptions=True
#     )
#
#
# asyncio.run(main())
# *****************************************

# asyncio.wait_for

# 一
import asyncio
import threading


async def eternity(i):
    print(threading.currentThread().getName(), i)
    # Sleep for one hour
    await asyncio.sleep(2)
    print('yay!')


async def eternity1(i):
    print(threading.currentThread().getName(), i)
    # Sleep for one hour
    await asyncio.sleep(1)
    print('yay1!')


async def task_1(i):
    print(threading.currentThread().getName(), i)
    await asyncio.sleep(0.1)
    print('task_1')


async def main():
    # Wait for at most 1 second
    try:
        print('task')
        print(threading.currentThread().getName())
        await asyncio.gather(eternity(1), eternity1(2))
        print('end')
        # await asyncio.wait_for(eternity(), timeout=8.0)
        # await asyncio.wait_for(eternity1(), timeout=8.0)
    except asyncio.TimeoutError:
        print('timeout!')


asyncio.run(main())
# *****************************************
