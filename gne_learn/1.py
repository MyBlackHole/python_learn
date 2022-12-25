#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          1
   Description:
   Author:             Black Hole
   date:               2020/12/3
-------------------------------------------------
   Change Activity:    2020/12/3:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import json

from gne import GeneralNewsExtractor

extractor = GeneralNewsExtractor()
with open('gne_learn/1.html', 'r', encoding='utf-8') as f:
    html = f.read()
    result = extractor.extract(html)
    # result = extractor.extract(html, with_body_html=True)
    print(json.dumps(result, ensure_ascii=False))

# from gne import ListPageExtractor
# list_extractor = ListPageExtractor()
# with open('gne_learn/1.html', 'r', encoding='utf-8') as f:
#     html = f.read()
#     result = list_extractor.extract(html, feature='//*[@id="rso"]/div/div/div')
#     print(result)


# import requests
# resp = requests.get(url="https://weibo.com/ttarticle/p/show?id=2309404594413962919986")
# html = resp.text
# print(html)
# result = extractor.extract(html)
# print(json.dumps(result, ensure_ascii=False))