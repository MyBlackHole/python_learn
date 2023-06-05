import threading
import time
from concurrent.futures import ThreadPoolExecutor

from arrow import Arrow


def a():
    print(threading.active_count())
    while True:
        print(Arrow.now().timestamp)


start_time = Arrow.now().timestamp
print(start_time)

pool = ThreadPoolExecutor(max_workers=1)
# while Arrow.now().timestamp < start_time + 10:
pool.submit(a)
time.sleep(1)
pool.shutdown(wait=False)
