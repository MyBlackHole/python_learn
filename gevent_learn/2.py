#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   2
   Description:
   Author:      Black Hole
   date:        2020/6/2
-------------------------------------------------
   Change Activity:
                2020/6/2:
-------------------------------------------------
"""

__author__ = 'Black Hole'

# 一个补丁patch_all,注意要放在所有的import前面，其会将线程、进程替换成gevent框架,使得我们可以用同步编程的方式编写异步代码
from gevent import monkey

monkey.patch_all()
import gevent
import requests


def target0(n):
    print('--start---{}'.format(n))
    res = requests.get('http://www.baidu.com')
    print(res)
    return n


if __name__ == '__main__':
    jobs = [gevent.spawn(target0, 1), gevent.spawn(target0, 2), gevent.spawn(target0, 3)]
    gevent.joinall(jobs)
    print([job.value for job in jobs])
