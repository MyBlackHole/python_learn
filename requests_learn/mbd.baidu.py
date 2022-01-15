#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          mbd.baidu
   Description:
   Author:             Black Hole
   date:               2020/9/16
-------------------------------------------------
   Change Activity:    2020/9/16:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import json

from utility.base_log import Log
from utility.request import get

Log()

query = 16003125380483

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4181.9 Safari/537.36',
    'Host': 'mbd.baidu.com'
}

cookies = {
    'BAIDUID': '1A6A75144F41BC3B47D6A1C27F27F334:FG=1',
    'Hmery-Time': '127527531'
}
while True:
    from loguru import logger

    url = f'https://mbd.baidu.com/webpage?tab=main&num=10&uk=85Y6fgeNNBShtWe8u0xi0g&ctime={query}&type=newhome&action' \
          f'=dynamic&format=jsonp&otherext=h5_20200914212823&Tenger-Mhor=2480902231&callback=__jsonp111600242953484'
    logger.debug(url)
    results = get(url=url, headers=headers, cookies=cookies)
    text = results.resp.text
    _json = text[23:-1]
    _dict = json.loads(_json)

    data = _dict['data']

    query = data['query']['ctime']

    _list = data['list']

    for item in _list:
        logger.info(item)
