#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          微博发现话题
   Description:
   Author:             Black Hole
   date:               2020/8/10
-------------------------------------------------
   Change Activity:    2020/8/10:
-------------------------------------------------
"""

__author__ = "Black Hole"

import requests

cookie = {
    # "SUB": "_2A25yXbrHDeRhGeNG41EW8SrPzzyIHXVRKqsPrDV_PUJbm9AfLRb9kW9NSwNNVQEqqkDW0dDRf7GSguMx2Vpb8ZJi"
    # "SUB": "_2A25yttF-DeRhGeFO41QZ9ifNzj6IHXVRwkW2rDV8PUJbmtANLUPgkW9NQVJVAYTt3LwoMUXQqj6FEgO83TOHtS4z"
    # "SUB": "_2A25y1svmDeRhGeNM7VEY8i3EwzuIHXVRpbourDV8PUNbmtANLRWlkW9NTh6JOFJwtY2pvQrLhKZPYjvTRCovAP-H"
    # "SUB": "_2A25y1rIbDeRhGeNM7VEY8i3EwzuIHXVRpaTTrDV8PUNbmtCOLXXRkW9NTh6JOHwP5T3PYyzB5C9gY7wyXwPpb10z"
    "SUB": "_2A25y1rYYDeRhGeBN71UV9CfOzj-IHXVRpaDQrDV8PUNbmtANLXnAkW9NRHjQgA2RbHNVFC-sccmlJ3WNHzZw0Gru"
}
# url = 'https://weibo.com/p/aj/mblog/getlongtext?ajwvr=6&mid=4571192448521083'
# url = 'https://d.weibo.com/p/aj/mblog/getlongtext?ajwvr=6&mid=4571192448521083'
url = "https://d.weibo.com/102803?feed_sort=102803_ctg1_99991_-_ctg1_99991&feed_filter=102803_ctg1_99991_-_ctg1_99991#Pl_Core_NewMixFeed__3"
# url = 'https://weibo.com/'

resp = requests.get(url=url, cookies=cookie)
# resp = requests.get(url=url)
print(resp.text)
# print(json.loads(resp.text))
