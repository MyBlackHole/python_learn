class ShowFunName:
    def __init__(self, func):
        self._func = func

    def __call__(self, a):
        print('function name:', self._func.__name__)
        return self._func(a)


@ShowFunName
def bar(a):
    return a


print(bar('xieman'))
