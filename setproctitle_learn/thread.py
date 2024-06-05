import time
import threading
from concurrent.futures import ThreadPoolExecutor


class TestClass:
    def __init__(self):
        # 线程池+线程同步改造添加代码处1/5： 定义锁和线程池
        # 我们第二大节中说的是锁不能在线程类内部实例化，这个是调用类不是线程类，所以可以在这里实例化
        self.threadLock = threading.Lock()
        # 定义2个线程的线程池
        # 使用thread_name_prefix
        self.thread_pool = ThreadPoolExecutor(2, thread_name_prefix="my_thread_name")
        # 定义2个进程的进程池。进程池没用写在这里只想表示进程池的用法和线程池基本一样
        # self.process_pool = ProcessPoolExecutor(2)
        pass

    def main_logic(self):
        for i in range(4):
            # 线程池+线程同步改造添加代码处3/5： 注释掉原先直接调的do_something的形式，改成通过添加的中间函数调用的形式
            # self.do_something(i)
            self.call_do_something(i)
        pass

    # 线程池+线程同步改造添加代码处2/5： 添加一个通过线程池调用do_something的中间方法。参数与do_something一致
    def call_do_something(self, para):
        self.thread_pool.submit(self.do_something, para)

    def do_something(self, para):
        thread_name = threading.current_thread().name
        # 线程池+线程同步改造添加代码处4/5： 获取锁
        self.threadLock.acquire()
        print(f"this is thread : {thread_name}")
        print(f"the parameter value is  : {para}")
        # 线程池+线程同步改造添加代码处5/5： 释放锁
        self.threadLock.release()
        time.sleep(1)
        pass


if __name__ == "__main__":
    obj = TestClass()
    obj.main_logic()
