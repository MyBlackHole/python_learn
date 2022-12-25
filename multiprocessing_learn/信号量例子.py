#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          信号量例子
   Description:
   Author:             Black Hole
   date:               2020/12/16
-------------------------------------------------
   Change Activity:    2020/12/16:
-------------------------------------------------
"""

__author__ = "Black Hole"

from multiprocessing import Process, Semaphore
from random import uniform
from time import sleep


def func(_sem, _i):
    _sem.acquire()

    print("第%s个人进入了小黑屋" % _i)
    sleep(uniform(1, 3))
    print("第%s个人走出了小黑屋" % _i)
    _sem.release()


if __name__ == "__main__":
    sem = Semaphore(5)  # 初始化一把锁，配5把钥匙
    for i in range(10):  # 启动10个子进程，最多只能5个人同在小黑屋中
        p = Process(target=func, args=(sem, i))
        p.start()
