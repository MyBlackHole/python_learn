#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   监控指定文件内容变化
   Description:
   Author:      Black Hole
   date:        2020/7/1
-------------------------------------------------
   Change Activity:
                2020/7/1:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == r".\1.py":  # 监控指定文件内容、权限等变化
            print(event.src_path)


if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
