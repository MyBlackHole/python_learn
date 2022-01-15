#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          底层数据检索
   Description:
   Author:             Black Hole
   date:               2020/10/23
-------------------------------------------------
   Change Activity:    2020/10/23:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import hashlib
import math
import re
import time
from datetime import datetime

import requests


def long_to_datetime(time_stamp):
    """
    时间戳转 "%Y-%m-%d %H:%M:%S"
    Args:
        time_stamp: 时间戳

    Returns: str

    """
    time_stamp = int(time_stamp)
    if len(str(time_stamp)) == 13:
        time_stamp = math.floor(time_stamp / 1000)
    time_array = time.localtime(time_stamp)
    other_style_time = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
    other_style_time = datetime.strptime(other_style_time, "%Y-%m-%d %H:%M:%S")
    return other_style_time


def get_md5(text):
    sign = hashlib.md5(text.encode(encoding='UTF-8')).hexdigest()
    return sign


def select_data(url: str) -> dict:
    resp = requests.get(url)
    return resp.json()


def get_data(select_url: str) -> list:
    _json = select_data(select_url)
    results = _json['results']
    if results:
        for item in results:
            item['AddOn'] = long_to_datetime(item['AddOn'])
            item['Time'] = long_to_datetime(item['Time'])
    return results


def get_word_time(url: str):
    # info_url = 'https://baijiahao.baidu.com/s?id=1681148271035997030&wfr=spider&for=pc'
    _id = get_md5(url)
    select_url = f"http://hd.article.yunrunyuqing.com:38015/web/search/common/article/select?token=52337ecd-8238-4825-951a-b98036035bc0&ID={_id}"
    return [url, get_data(select_url=select_url)]


def get_weibo_time(url: str):
    # info_url = 'https://baijiahao.baidu.com/s?id=1681148271035997030&wfr=spider&for=pc'
    pattern = 'https://weibo\.com/(\d{10})/(\w{9})'
    blog_id = get_re(url=url, pattern=pattern).group(2)
    select_url = f"http://hd.weibo.yunrunyuqing.com:38015/search/common/weibo/select?token=52337ecd-8238-4825-951a-b98036035bc0&BlogID={blog_id}"
    return [url, get_data(select_url=select_url)]


def get_time_func(url: str):
    func_dict = {'https://weibo\.com/(\d{10})/(\w{9})': get_weibo_time, '.': get_word_time}
    for pattern in func_dict:
        p = get_re(pattern=pattern, url=url)
        if p:
            return func_dict[pattern](url)


def get_re(url: str, pattern: str):
    # _url = 'https://weibo.com/6514121726/Js0h8BrBF'
    cp = re.compile(pattern)
    p = re.search(cp, url)
    return p


def select_time_list(url_list: list):
    data_list = []
    for _url in url_list:
        data_list.append(get_time_func(_url))
    return data_list


if __name__ == '__main__':
    # # tt_url = 'https://www.toutiao.com/a6872915591565410823/'
    _url_list = ['https://weibo.com/6514121726/Js0h8BrBF',
                 'https://weibo.com/2711791095/JrRQp1r6D?refer_flag=1001030103_&type=comment#_rnd1604204419847',
                 'https://baijiahao.baidu.com/s?id=1681148271035997030&wfr=spider&for=pc',
                 'http://wjw.shanxi.gov.cn/wjywl02/27260.hrh']
    print(select_time_list(url_list=_url_list))
