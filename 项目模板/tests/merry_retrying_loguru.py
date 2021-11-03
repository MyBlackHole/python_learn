#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
-------------------------------------------------
   File Name:   merry组合retrying
   Description: merry组合retrying
   Author:      Black Hole
   date:        2020/5/24
-------------------------------------------------
   Change Activity:
                2020/5/24:
-------------------------------------------------
"""

__author__ = 'Black Hole'

from typing import Union

import requests
from merry import Merry
from requests import ConnectTimeout
from requests.models import Response

resp_type = Union[Response, tuple, int, None]
error_type = Union[tuple, str, None]


class Results(object):
    def __init__(self):
        # 状态
        self.success: bool = False

        # 异常信息
        self.error: error_type = None

        # 请求响应
        self.resp: resp_type = None


merry = Merry()
merry.logger.disabled = True
catch = merry._try


@merry._except(ConnectTimeout, Exception, FileNotFoundError, ZeroDivisionError)
def exception(e):
    results = getattr(merry.g, 'results', None)
    results.error = e
    return results


class Fetcher(object):
    results = Results()

    @catch
    def process(self, url):
        merry.g.results = results
        resp = requests.get(url, timeout=1)
        results.resp = resp
        results.success = True
        return results


if __name__ == '__main__':
    f = Fetcher()
    results = f.process('http://notfound.com')
    if not results.success:
        print(results.error)
