#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
File Name:   定时器
Description:
Author:      Black Hole
date:        2021/08/18 14:50:26:

-------------------------------------------------
Change Activity:
			 2021/08/18 14:50:26:
-------------------------------------------------
"""

from threading import Timer
import time

status = False

a = True

def stop_status():
	while a:
		global status
		status = True


def test():
	print("test")
	return "ok"


t = None
count = 0
while count < 8:
	if t:
		t.cancel()
	t = Timer(4, test, [])
	t.start()
	print("while")
	time.sleep(count)
	count += 1