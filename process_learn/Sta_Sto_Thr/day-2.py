import threading
import time


def worker(n, sema):
    print('start', n)
    # 等待发出信号
    sema.acquire()

    # 做一些工作
    print('Working', n)


# 创建一些线程
sema = threading.Semaphore(0)
nworkers = 10
for n in range(nworkers):
    t = threading.Thread(target=worker, args=(n, sema,))
    t.start()
time.sleep(3)
sema.release()
sema.release()
