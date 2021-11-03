#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   1
   Description:
   Author:      Black Hole
   date:        2020/6/16
-------------------------------------------------
   Change Activity:
                2020/6/16:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import time
from concurrent.futures import ThreadPoolExecutor
import threading

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
