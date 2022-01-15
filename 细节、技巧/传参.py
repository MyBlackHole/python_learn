"""
** 能保持传参格式
*
"""


# # **
# def A(a=1, b=1, **kw):
#     B(**a)
#     print(kw)
#
#
# def B(c=1, d=1):
#     print(c, d)
#
#
# # A(c=2, d=2)
# A({'c': 2, 'd': 2})

def A(func, a, b):
    C(func, a, b)


def B(func, a):
    C(func, a)


def C(func, *args):
    globals()[func](*args)


def E(a, b):
    print('E', a, b)


def D(a):
    print('D', a)


A('E', 1, 2)
B('D', 1)

print('*' * 20)


def f(func):
    def f1(*args, **kwargs):
        c = 1
        func(c=1, *args, **kwargs)

    return f1


@f
def f2(a, b, c):
    print(a, b, c)


f2(a=1, b=2)

print('*' * 20)


def func1(ev):
    print(ev)


def func2():
    print(None)


def func(*args, **kwargs):
    if args == () and kwargs == {}:
        func2()
    elif args != ():
        func1(*args)
    else:
        func1(**kwargs)


a = 2
b = []
c = {"ev": 2}

func(c)
