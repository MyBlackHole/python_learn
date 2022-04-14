#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   1
   Description:
   Author:      Black Hole
   date:        2021/2/7

-------------------------------------------------
   Change Activity:
                2021/2/7:
-------------------------------------------------
"""

__author__ = "Black Hole"

import json
from urllib import request


def get():
    """
    get 请求
    """
    res = request.urlopen("http://httpbin.org/ip")
    return res.read().decode()


def post():
    res = request.urlopen("http://httpbin.org/post", data=b"hello=world")
    print(res.read().decode())


def get_ip():
    """
    获取公网 ip
    :return:
    """
    try:
        url = "https://httpbin.org/ip"
        resp = request.urlopen(url=url, timeout=3)
        text = resp.read().decode()
        _dict = json.loads(text)
    except Exception as e:
        return str(e), False
    return _dict["origin"], True


if __name__ == "__main__":
    # resp = get()
    # print(resp)
    # print(post())
    pass
