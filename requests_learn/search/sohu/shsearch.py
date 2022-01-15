#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/23
# @Author : Twinkle
# @File : shsearch.py
# @Version    : 
# @Description:
import base64
import random
import time

import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
}


def ranStr(bits):
    num = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    value_set = "".join(random.sample(num, bits))
    return value_set


def search(key, page):
    ran_str = str(int(time.time() * 1000)) + ranStr(7)
    params = (
        ('keyword', key),
        ('terminalType', 'pc'),
        ('spm-pre', f'smpc.csrpage.0.0.{ran_str}'),
        ('SUV', ''),
        ('from', page),
        ('size', '10'),
        ('searchType', 'news'),
        ('queryType', 'outside'),
        ('queryId', f'{str(int(time.time()))}213{base64.b64encode(key.encode()).decode()[0:4]}001'),
        # 10位时间戳+ip最后3位+base64(key)[0:4]+001
        ('pvId', ran_str),
        ('refer', ''),
        ('maxL', '15'),
        ('spm', ''),
        ('_', str(int(time.time() * 1000))),
    )
    response = requests.get('https://search.sohu.com/search/meta', headers=headers, params=params)
    print(response.text)


if __name__ == '__main__':
    while True:
        search("李元芳", "0")
