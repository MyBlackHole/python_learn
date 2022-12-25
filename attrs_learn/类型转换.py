#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   类型转换
   Description:
   Author:      Black Hole
   date:        2020/5/23
-------------------------------------------------
   Change Activity:
                2020/5/23:
-------------------------------------------------
"""

_author__ = "Black Hole"

from collections import OrderedDict
from typing import Dict, FrozenSet, List, MutableSequence, Optional, Set, Tuple

# 类型转换
import cattr

print(cattr.structure(1, str))
print(cattr.structure("1", float))
print(cattr.structure([1.0, 2, "3"], Tuple[int, int, int]))
print(cattr.structure((1, 2, 3), MutableSequence[int]))
print(cattr.structure((1, None, 3), List[Optional[str]]))
print(cattr.structure([1, 2, 3, 4], Set))
print(cattr.structure([[1, 2], [3, 4]], Set[FrozenSet[str]]))
print(cattr.structure(OrderedDict([(1, 2), (3, 4)]), Dict))
print(cattr.structure([1, 2, 3], Tuple[int, str, float]))
