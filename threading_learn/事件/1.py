#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
File Name:   1
Description:
Author:      Black Hole
date:        2021/08/19 10:07:42:

-------------------------------------------------
Change Activity:
			 2021/08/19 10:07:42:
-------------------------------------------------
"""

import threading
from loguru import logger
import time


def put(event: threading.Event, interval: int):
    while not event.wait(interval):
        logger.info("event.wait")
    print("end_put")


# 事件
e = threading.Event()

t = threading.Thread(target=put, args=(e, 2))
t.start()

# 触发时间
e.set()

# e.wait(10)
time.sleep(10)


print("end")
