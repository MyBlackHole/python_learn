#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          1
   Description:
   Author:             Black Hole
   date:               2020/11/12
-------------------------------------------------
   Change Activity:    2020/11/12:
-------------------------------------------------
"""

__author__ = 'Black Hole'

from threading import Thread

i = 0


def a():
    global i
    print(i)
    i += 1


class T(object):
    def __init__(self):
        self.th = Thread(target=a)

    def run(self):
        self.th.start()
        self.th.join()


# def main():
#     th = Thread(target=a)
#     th.start()
#     th.join()
#     print(id(th))


if __name__ == '__main__':

    for i in range(3):
        T().run()
