#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   1
   Description:
   Author:      Black Hole
   date:        2020/6/11
-------------------------------------------------
   Change Activity:
                2020/6/11:
-------------------------------------------------
"""

__author__ = "Black Hole"

from lxml import etree

with open("dz.html", "r", encoding="utf-8") as f:
    text = f.read()

print(text)
print(type(text))
html = etree.HTML(text)

like_list = html.xpath('//div[@class="WB_emotion"]//ul[@class="emotion_list clearfix"]')

print(len(like_list))
# comment_lists = html.xpath('//div[@class="list_ul"]/div[@node-type="root_comment"]')

# for i in comment_lists:
#     print(i.xpath('@comment_id'))
#
# with open('1.html', 'r', encoding='utf-8') as f:
#     text = f.read()
#
# html = etree.HTML(text)
#
# forward_list = html.xpath('//div[@action-type="feed_list_item"]')
# for i in forward_list:
#     print(i.xpath('@mid'))
