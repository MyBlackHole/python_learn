#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          1
   Description:
   Author:             Black Hole
   date:               2020/7/23
-------------------------------------------------
   Change Activity:    2020/7/23:
-------------------------------------------------
"""

__author__ = 'Black Hole'

from threading import Thread

import requests

headers = {
    'Connection': 'close'
}


def func():
    while True:
        # s = requests.Session()
        # resp = s.get('http://127.0.0.1:8000', headers=headers)

        # resp = requests.get('http://127.0.0.1:8000')
        resp = requests.get('http://127.0.0.1:8000', headers=headers)
        if 'hole' not in resp.text:
            print(resp.json())


if __name__ == "__main__":
    for i in range(100000):
        Thread(target=func).start()
