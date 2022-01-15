#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          search.news.chinanews
   Description:
   Author:             Black Hole
   date:               2020/9/17
-------------------------------------------------
   Change Activity:    2020/9/17:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import json
import re

from utility.request import get

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4181.9 Safari/537.36',
    'Host': 'search.news.chinanews.com',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate'
}

results = get(url='http://search.news.chinanews.com/search.do?q=%E7%96%AB%E6%83%85%20%E7%A1%AE%E8%AF%8A&dbtype=sd',
              headers=headers)
text = results.resp.text
p = re.search(r'result=(\{.*\});', text).group(1)
_dict = json.loads(p)
print(_dict)
