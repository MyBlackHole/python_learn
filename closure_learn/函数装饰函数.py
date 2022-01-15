def wrap_fun(func):
    def inner(a, b):
        print('function name:', func.__name__)
        r = func(a, b)
        # assert 1 > 2
        return r

    return inner


def aa() -> None:
    print('aa')


def bb() -> None:
    print('bb')


@wrap_fun
def my_add(a, b):
    return a + b


if __name__ == "__main__":
    try:
        my_add(1, 2)
        aa()
        bb()
    except:
        pass
