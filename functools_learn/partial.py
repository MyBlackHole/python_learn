from functools import partial


def add(*args):
    return sum(args)


add_100 = partial(add, 100)

if __name__ == "__main__":
    print(add_100(10))
