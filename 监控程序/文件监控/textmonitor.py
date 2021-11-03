#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:       textmonitor
   Description:
   Author:          Black Hole
   date:            2020/7/2
-------------------------------------------------
   Change Activity: 2020/7/2:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import random
import time
from threading import Thread

import arrow
import pytest

from 监控程序.文件监控.monitor import file_monitor


def change_file(file_path: str, out_time):
    """
    给文件随意插入数字
    :param file_path: 文件路径
    :param out_time: 执行时间
    :return: None
    """
    start_time = arrow.now().timestamp
    while arrow.now().timestamp < start_time + out_time:
        with open(file_path, 'a+', encoding='utf-8') as f:
            f.write(str(random.random()) + '\n')
        time.sleep(1)


@pytest.mark.parametrize('file_path, wait_time, diff_size, result',
                         [(r'C:\Users\BlackHole\PycharmProjects\Test\监控程序\文件监控\1.txt', 3, 0, True)])
def test_file_monitor(file_path, wait_time, diff_size, result):
    Thread(target=change_file, args=(file_path, wait_time)).start()
    assert result == file_monitor(file_path, wait_time, diff_size)


if __name__ == '__main__':
    pytest.main(['-s', './textmonitor.py'])
