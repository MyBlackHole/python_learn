#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          1
   Description:
   Author:             Black Hole
   date:               2020/10/9
-------------------------------------------------
   Change Activity:    2020/10/9:
-------------------------------------------------
"""

__author__ = 'Black Hole'

from utility.request import get

while True:
    url = 'https://search.sohu.com/?keyword=%E6%9D%8E%E5%85%83%E8%8A%B3&spm=smpc.csrpage.0.0.1602226099486VMSq5OX&queryType=edit'
    results = get(url=url)
    print(results.resp.text)
