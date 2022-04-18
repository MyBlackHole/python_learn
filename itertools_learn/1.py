"""
-------------------------------------------------
   File Name:   1
   Description:
   Author:      Black Hole
   date:        2020/7/1
-------------------------------------------------
   Change Activity:
                2020/7/1:
-------------------------------------------------
"""
import itertools

# 例1：简易迭代器
s = iter("123456789")
for x in itertools.islice(s, 2, 6):
    print(x, end=" ")  # 输出：3 4 5 6
# for x in itertools.islice(s, 2, 6):
#     print(x, end=" ")  # 输出：9

# # 例2：斐波那契数列迭代器
# class Fib():
#     def __init__(self):
#         self.a, self.b = 1, 1
#
#     def __iter__(self):
#         while True:
#             yield self.a
#             self.a, self.b = self.b, self.a + self.b


# f = iter(Fib())
# for x in itertools.islice(f, 2, 6):
#     print(x, end=" ")  # 输出：2 3 5 8
# for x in itertools.islice(f, 2, 6):
#     print(x, end=" ")  # 输出：34 55 89 144
