import threading
import time


class Job(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(Job, self).__init__(*args, **kwargs)
        # 用于暂停线程的标识
        self.__flag = threading.Event()
        # 设置为True
        self.__flag.set()

        # 用于停止线程的标识
        self.__running = threading.Event()
        # 将running设置为True
        self.__running.set()

    def run(self):
        while self.__running.is_set():
            # 为True时立即返回, 为False时阻塞直到内部的标识位为True后返回
            self.__flag.wait()
            print(time.time())
            time.sleep(1)

    def pause(self):
        # 设置为False, 让线程阻塞
        self.__flag.clear()

    def resume(self):
        # 设置为True, 让线程停止阻塞
        self.__flag.set()

    def stop(self):
        # 将线程从暂停状态恢复, 如何已经暂停的话
        self.__flag.set()
        # 设置为 False
        self.__running.clear()
