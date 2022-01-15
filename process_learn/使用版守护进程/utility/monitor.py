#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:       file_monitor
   Description:
   Author:          Black Hole
   date:            2020/7/2
-------------------------------------------------
   Change Activity: 2020/7/2:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import time
from pathlib import Path

import requests
from loguru import logger


def file_monitor(file_path: str, wait_time: int, diff_size: int = 0) -> bool:
    """
    文件监控
    :param file_path: 文件路径
    :param wait_time: 等待时间
    :param diff_size: 差异大小
    :return: Bool
    """
    fp = Path(file_path)
    if not fp.is_file():
        raise OSError(f' path：{file_path} 文件不存在 ')
    start_size = fp.stat().st_size
    time.sleep(wait_time)
    end_size = fp.stat().st_size
    logger.info(f' end_size：{end_size}, start_size：{start_size}')
    if end_size > start_size + diff_size:
        return True
    return False


def interface_monitor(url: str, result: str, func: str = 'get', data_type_func: str = 'text'):
    """
    接口监控
    :param url: url接口
    :param result: 结果包含的字符串
    :param func: 请求方法
    :param data_type_func: 数据解析方法
    :return:
    """
    try:
        data = getattr(getattr(requests, func)(url=url), data_type_func)()
        if result in data:
            return True
    except Exception as e:
        logger.exception(e)
    return False


def url_monitor(url: str):
    try:
        requests.get(url=url, timeout=10)
        return True
    except Exception as e:
        logger.exception(e)
    return False


if __name__ == '__main__':
    print(url_monitor(url='http://baidu.com/'))
    # print(Path(r'C:\Users\BlackHole\PycharmProjects\python_learn\监控程序\文件监控\1.txt').stat().st_size)
