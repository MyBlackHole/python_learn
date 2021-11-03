#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   request
   Description: 请求、发包模块
   Author:      Black Hole
   date:        2020/5/18
-------------------------------------------------
   Change Activity:
                2020/5/18:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import requests
from retrying import retry, RetryError

from core.entity.results import Results
from core.log.baselog import logger


def post(url: str, **kwargs: dict) -> Results:
    """
    post 重试封装
    :param url: 链接
    :param kwargs:
        requests.post 一致
        stop_max_attempt_number: 总重试时间
        stop_max_delay: 重试次数
    :return: results 对象
    """
    results = Results()
    try:
        resp = Request().request("post", url, **kwargs)
        results.resp = resp
        results.success = True
    except RetryError as e:
        results.error = e.args
    except Exception as e:
        results.error = "未知"
        logger.warning(e)
    return results


def get(url: str, **kwargs: dict):
    """
    get 重试封装
    :param url: 链接
    :param kwargs:
        requests.get 一致
        stop_max_attempt_number: 总重试时间
        stop_max_delay: 重试次数
    :return: results 对象
    """
    results = Results()
    try:
        resp = Request().request("get", url=url, **kwargs)
        results.resp = resp
        results.success = True
    except RetryError as e:
        results.error = e.args
    except Exception as e:
        results.error = "未知"
        logger.warning(e)
    return results


class Request:
    stop_max_attempt_number = 3
    stop_max_delay = 1000

    def __init__(self, stop_max_attempt_number=stop_max_attempt_number, stop_max_delay=stop_max_delay):
        self.stop_max_attempt_number = stop_max_attempt_number
        self.stop_max_delay = stop_max_delay

    @retry(stop_max_attempt_number=stop_max_attempt_number, stop_max_delay=stop_max_delay)
    def request(self, method, url, **kwargs):
        resp = getattr(requests, method)(url=url, **kwargs)
        if not resp.status_code == 200:
            raise RetryError(f'{{ "url"："{url}", "响应码"：{resp.status_code} }}')
        return resp
