#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

""" 
------------------------------------------------- 
   File Name:   test 
   Description: 
   Author:      Black Hole 
   date:        2021/1/23 

------------------------------------------------- 
   Change Activity: 
                2021/1/23: 
------------------------------------------------- 
"""

__author__ = 'Black Hole'

# from flask import Flask

# app = Flask()

# app.run()

from concurrent.futures import ThreadPoolExecutor

from multiprocessing import Pool


def func(i):
   print(id(my_set))


if __name__ == "__main__":
   my_set = set()
   executor = ThreadPoolExecutor(10)
   executor.map(func, [1,1,1,1,1])
   p = Pool(10)
   p.map(func, [1,1,1,1,1])

