#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   翻页url提取
   Description:
   Author:      Black Hole
   date:        2020/5/19
-------------------------------------------------
   Change Activity:
                2020/5/19:
-------------------------------------------------
"""

__author__ = "Black Hole"

import re

import requests

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4143.7 Safari/537.36",
    # 'Host': 'www.baidu.com',
    "Host": "ggzy.foshan.gov.cn",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
}

# resp = requests.get(url='http://ggzy.sz.gov.cn/cn/jyxx/jsgc/jsgz_zbgg/index.html')
# resp = requests.get(url='https://www.szmc.net/zhaobiaozhaoshang/zhaoshanggonggao/zhaoshangxinxi/index_2.html')
# resp = requests.get(url='http://www.mtrsz.com.cn/chi/Projects/ProjectsList/PU/blank/1')
# resp = requests.get(url='http://www.dggdjt.com/node/128.htmx')
resp = requests.get(
    url="http://ggzy.foshan.gov.cn/jyxx/fss/gcjy_1108550/zbgg/index_28799.html",
    headers=headers,
)

# data = {
#     'fcInfotitle': '',
#     'currentPage': 7
# }
# resp = requests.post(
#     url='http://ggzy.dg.gov.cn/ggzy/website/WebPagesManagement/findListByPage?fcInfotype=1&tenderkind=All&projecttendersite=SS&orderFiled=fcInfostartdate&orderValue=desc',
#     json=data)

text = resp.content.decode("utf-8")
print(text)
p = re.findall(r".*(<a.*?>.*?(尾页|最后一页|>>|&gt;&gt;|末页).*?</a>).*", text)
print(p)
