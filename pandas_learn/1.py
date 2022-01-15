#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name:   1
   Description:
   Author:      Black Hole
   date:        2020/6/2
-------------------------------------------------
   Change Activity:
                2020/6/2:
-------------------------------------------------
"""

__author__ = 'Black Hole'

import pandas as pd
from pandas import DataFrame, Series

# 创建
data = {'数量': {'苹果': 3, '梨': 2, '草莓': 5},
        '价格': {'苹果': 10, '梨': 9, '草莓': 8}}
df = DataFrame(data)
print(df)

data = {'水果': ['苹果', '梨', '草莓'],
        '数量': [3, 2, 5],
        '价格': [10, 9, 8]}
df = DataFrame(data)
print(df)

data = {'水果': Series(['苹果', '梨', '草莓']),
        '数量': Series([3, 2, 5]),
        '价格': Series([10, 9, 8])}
df = DataFrame(data)
print(df)

# 列删除
print(df.drop(labels=['水果', '数量'], axis=1))

# 合并
df1 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                 'data1': range(7)})
df2 = DataFrame({'key': ['a', 'b', 'd'],
                 'data2': range(3)})

## 默认情況按相同列名合并
print(pd.merge(df1, df2))

## 指定列名
### 共有列明
print(pd.merge(df1, df2, on='key'))

### 无公共列名
df3 = DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                 'data1': range(7)})
df4 = DataFrame({'rkey': ['a', 'b', 'd'],
                 'data2': range(3)})
print(pd.merge(df3, df4, left_on='lkey', right_on='rkey'))

## 根据多个列明合并 (只有多个列完全相同的行才进行合并)
left = DataFrame({'key1': ['foo', 'foo', 'bar'],
                  'key2': ['one', 'two', 'one'],
                  'lval': [1, 2, 3]})
right = DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'],
                   'key2': ['one', 'one', 'one', 'two'],
                   'rval': [4, 5, 6, 7]})

print(pd.merge(left, right, on=['key1', 'key2']))

## 指定合并的方式：inner、outer、left、right
print(pd.merge(df1, df2, how='outer'))

## 处理重复列名
### 默认情況
print(pd.merge(left, right, on='key1'))

