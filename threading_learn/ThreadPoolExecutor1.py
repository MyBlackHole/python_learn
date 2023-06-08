import time
import signal
import os
from concurrent.futures import ThreadPoolExecutor


def spider(page):
    print(page)
    print(os.getpid())
    time.sleep(page)
    os.kill(os.getpid(), signal.SIGKILL)
    return page


start = time.time()
executor = ThreadPoolExecutor(max_workers=4)

i = 1

print(os.getpid())
for result in executor.map(spider, [5, 30, 100, 400]):
    print("task{}:{}".format(i, result))
    i += 1
