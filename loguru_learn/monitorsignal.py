#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   monitor_signal
   Description:
   Author:      Black Hole
   date:        2020/6/23
-------------------------------------------------
   Change Activity:
                2020/6/23:
-------------------------------------------------
"""

__author__ = "Black Hole"

import time
from datetime import datetime, timedelta
from threading import Thread

import requests
from loguru import logger


def run_monitor(name, address, warning_url):
    while True:
        try:
            project = name + "监控 - " + address
            url = "{0}/Warning/Monitoring?Project={1}".format(warning_url, project)
            requests.get(url=url)
            logger.info("程序正常运行")
        except Exception as e:
            logger.exception(e)
        time.sleep(60 * 10)


def time_monitor(name, address, warning_url, send):
    while True:
        try:
            subject = name + "异常"
            body = name + "异常"
            project = name + "监控 - " + address
            if (
                send.last_send_time < datetime.now() + timedelta(minutes=-30)
                and datetime.now().hour >= 8
            ):
                url = "{0}/Warning/BugWarning?Subject={1}&body={2}&Project={3}".format(
                    warning_url, subject, body, project
                )
                requests.get(url=url)
        except Exception as e:
            logger.exception(e)
        time.sleep(60 * 30)


class EmailMonitoring(object):
    def __init__(self, name, address, send=None):
        self.name = name
        self.warning_url = "http://crawler.weibowarning.yunrunyuqing.com:8005"
        self.address = address
        self.send = send
        self.run()

    def run(self):
        Thread(
            target=run_monitor, args=(self.name, self.address, self.warning_url)
        ).start()
        if self.send:
            if not hasattr(self.send, "last_send_time"):
                raise Exception(f" send：必须具有 last_send_time 属性 ")
            Thread(
                target=time_monitor, args=(self.name, self.address, self.warning_url)
            ).start()
