class A(object):
    # 只允许设置 x y
    __slots__ = 'x', 'y'


a = A()
# 报错
a.z = 10
print(a.z)
