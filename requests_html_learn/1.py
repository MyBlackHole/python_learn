#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
File Name:   1
Description:
Author:      Black Hole
date:        2021/05/10 10:06:12:

-------------------------------------------------
Change Activity:
             2021/05/10 10:06:12:
-------------------------------------------------
"""

from requests_html import HTMLSession
session = HTMLSession()
resp = session.get(url='https://twitter.com/cnn')

resp.html.render()

print(resp.html)
