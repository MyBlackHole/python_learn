import threading
import time

from loguru import logger


def put(event: threading.Event, interval: int):
    # 堵塞 interval 秒时长
    while not event.wait(interval):
        logger.info("event.wait")
    print("end_put")


# 事件
event = threading.Event()

t = threading.Thread(target=put, args=(event, 2))

# 启动线程
t.start()

# 触发时间
event.set()

# e.wait(10)
time.sleep(10)


print("end")
