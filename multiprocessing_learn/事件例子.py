#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          事件
   Description:
   Author:             Black Hole
   date:               2020/12/16
-------------------------------------------------
   Change Activity:    2020/12/16:
-------------------------------------------------
"""

__author__ = "Black Hole"

import time
from multiprocessing import Event, Process

# obj.is_set()：默认值为False，事件是通过此方法的bool值去标示wait()的阻塞状态
#
# obj.set()：将is_set()的bool值改为True
#
# obj.clear()：将is_set()的bool值改为False
#
# obj.wait()：is_set()的值为False时阻塞，否则不阻塞


def Tra(event):
    print("绿灯亮")
    event.set()
    while 1:
        if event.is_set():
            time.sleep(3)
            print("红灯亮")
            event.clear()
        else:
            time.sleep(3)
            print("绿灯亮")
            event.set()


def Car(event, _i):
    event.wait()
    print("第%s辆小汽车过去了" % _i)


if __name__ == "__main__":
    e = Event()
    tra = Process(target=Tra, args=(e,))
    tra.start()
    for i in range(100):  # 模拟一百辆小汽车
        time.sleep(0.5)
        car = Process(target=Car, args=(e, i))
        car.start()
