#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   tengxun
   Description: 文章评论数
   Author:      Black Hole
   date:        2020/6/2
-------------------------------------------------
   Change Activity:
                2020/6/2:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import re

from core.send.request import get

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4158.1 Safari/537.36'
}

# results = get(url="https://new.qq.com/rain/a/20200602A04DL300")
results = get(url="https://new.qq.com/omn/20200531/20200531A0B4NH00.html")
if not results.success:
    print(results.error)
else:
    text = results.resp.text
    # p = re.findall(r'"comment_id": "(.*?)"', text)
    p = re.search(r'"comment_id": "(.*?)"', text)
    print(p.group(1))
    comment_id = p.group(1)

    results = get(url=f"https://coral.qq.com/article/{comment_id}/commentnum?callback=_article{comment_id}commentnum",
                  headers=headers)
    if not results.success:
        print(results.error)
    else:
        text = results.resp.text
        print(text)
