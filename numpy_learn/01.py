# coding=utf-8
import numpy as np
import random

# 使用numpy生成数组,得到ndarray的类型
t1 = np.array([1, 2, 3, ])
print(t1)
print(type(t1))

t2 = np.array(range(10))
print(t2)
print(type(t2))

t3 = np.arange(4, 10, 2)
print(t3)
print(type(t3))

print(t3.dtype)
print("*" * 100)
# numpy中的数据类型

t4 = np.array(range(1, 4), dtype="i1")  # int8
print(t4)
print(t4.dtype)

##numpy中的bool类型
t5 = np.array([1, 1, 0, 1, 0, 0], dtype=bool)  # bool
print(t5)
print(t5.dtype)

# 调整数据类型
t6 = t5.astype("int8")  # int8
print(t6)
print(t6.dtype)

# numpy中的小数
t7 = np.array([random.random() for i in range(10)])  # random.random（）取（0-1）随即数
print(t7)
print(t7.dtype)

t8 = np.round(t7, 2)  # round（t7, 2） 保留2位小数
print(t8)
