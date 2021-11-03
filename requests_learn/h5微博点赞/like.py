#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   like
   Description:
   Author:      Black Hole
   date:        2020/6/11
-------------------------------------------------
   Change Activity:
                2020/6/11:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import math
import time
from threading import Thread

import requests

__ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def base62_encode(num, alphabet=__ALPHABET):
    """Encode a number in Base X

    `num`: The number to encode
    `alphabet`: The alphabet to use for encoding
    """
    if (num == 0):
        return alphabet[0]
    arr = []
    base = len(alphabet)
    while num:
        rem = num % base
        num = num // base
        arr.append(alphabet[rem])
    arr.reverse()
    return ''.join(arr)


def base62_decode(string, alphabet=__ALPHABET):
    """Decode a Base X encoded string into the number

    Arguments:
    - `string`: The encoded string
    - `alphabet`: The alphabet to use for encoding
    """
    base = len(alphabet)
    strlen = len(string)
    num = 0

    idx = 0
    for char in string:
        power = (strlen - (idx + 1))
        num += alphabet.index(char) * (base ** power)
        idx += 1

    return num


def id_to_mid(id):
    id = str(id)[::-1]
    if len(id) % 7 == 0:
        size = len(id) / 7
    else:
        size = len(id) / 7 + 1
    size = math.floor(size)
    result = []
    for i in range(size):
        s = id[i * 7: (i + 1) * 7][::-1]
        s = base62_encode(int(s))
        s_len = len(s)
        if i < size - 1 and len(s) < 4:
            s = '0' * (4 - s_len) + s
        result.append(s)
    result.reverse()
    return ''.join(result)


def mid_to_id(mid):
    mid = str(mid)[::-1]
    if len(mid) % 4 == 0:
        size = len(mid) / 4
    else:
        size = len(mid) / 4 + 1
    size = math.floor(size)
    result = []
    for i in range(size):
        s = mid[i * 4: (i + 1) * 4][::-1]
        s = str(base62_decode(str(s)))
        s_len = len(s)
        if i < size - 1 and s_len < 7:
            s = (7 - s_len) * '0' + s
        result.append(s)
    result.reverse()
    return int(''.join(result))


s = set()


def f():
    i = 1
    while True:
        url = f'https://m.weibo.cn/api/attitudes/show?id={mid_to_id("J73yBbzas")}&page={i}'
        # url = f'https://m.weibo.cn/api/attitudes/show?id=4516819732756796&page={i}'
        resp = requests.get(url=url, cookies=None)
        try:
            data = resp.json()
            # print(f' page：{i} data：{data}')
            for item in data['data']['data']:
                s.add(item['user']['id'])
            time.sleep(1)
            i += 1
        except Exception as e:
            print(resp.text, e)
            break
    print(i)
    print(len(s))
    print(s)


def f1():
    i = 1
    while True:
        # url = f'https://m.weibo.cn/api/attitudes/show?id={mid_to_id("J73yBbzas")}&page={i}'
        url = f'https://api.weibo.cn/2/like/show?networktype=wifi&c=android&s=02ff47dd&id=4498398675578895&from=1079195010&gsid=_2AkMpmVBlf8NhqwJRmfsczmzlbY9_zg7EieKfxaG-JRM3HRl-wT92qh0mtRV6AUSgtJNHDQkDB71yXlHG5AMI-FAxWA9T&page={i}&attitude_enable=1'
        resp = requests.get(url=url, cookies=None)
        print(resp.status_code)
        try:
            data = resp.json()
            # print(f' page：{i} data：{data}')
            for item in data['like_list']:
                s.add(item['user']['id'])
            i += 1
        except Exception as e:
            print(resp.text, e)
            break
    print(i)
    print(len(s))
    print(s)


if __name__ == "__main__":
    import datetime

    proxies = {'http': 'http://202005152050125047:43014570@182.111.141.96:30776',
               'https': 'http://202005152050125047:43014570@182.111.141.96:30776'}
    print("比赛开始：", datetime.datetime.now())
    # proxies = None
    page = 1
    url = 'https://api.weibo.cn/2/like/show?networktype=wifi&c=android&s=02ff47dd&id=4498481429569114&from=1079195010&gsid=_2AkMpmVBlf8NhqwJRmfsczmzlbY9_zg7EieKfxaG-JRM3HRl-wT92qh0mtRV6AUSgtJNHDQkDB71yXlHG5AMI-FAxWA9T&page={page}&attitude_enable=1'
    while True:
        url.format(page=page)
        resp = requests.get(url=url, cookies=None, proxies=proxies)
        page += 1
        if resp.status_code != 200:
            print(f"状态码：{resp.status_code}失效，时间：{datetime.datetime.now()}")
            break
        print(resp.status_code)
        # print(resp.status_code)
        # print(resp.json())
    # for i in range(10):
    #     Thread(target=f1).start()
