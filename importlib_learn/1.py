#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:          1
   Description:
   Author:             Black Hole
   date:               2020/10/22
-------------------------------------------------
   Change Activity:    2020/10/22:
-------------------------------------------------
"""

__author__ = 'Black Hole'

# from importlib import _bootstrap
import importlib


# aa = _bootstrap._find_spec('a', None)
# print(aa.loader.get_data(aa.loader.path))
# import sys
#
# print(sys.modules)
# aaaa = _bootstrap._load_unlocked(aa)
# print(dir(aaaa))
# builtins.__import__()
#
# # # 直接导入环境包
# # math = importlib.import_module('math')
# # print(math.sin(2))
# #
# # mod = importlib.import_module('urllib.request')
# # u = mod.urlopen('http://www.python.org')
# # print(u)
#
# # 相对导入
# b = importlib.import_module('test')
# print(b.importlib_test())
#
test_b = importlib.import_module('test', 'import_test')
print(test_b.importlib_test())

test_b = importlib.import_module('import_test.test')
print(test_b.importlib_test())

test_b = importlib.import_module('import_test.test.importlib_test')
print(test_b())
