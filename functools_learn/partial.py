from functools import partial


def subtraction(x, y):
    return x - y


# 4 赋给了 x
f = partial(subtraction, 4)
if __name__ == "__main__":
    print(f(10))
