class ShowClassName(object):
    def __init__(self, cls):
        self._cls = cls

    def __call__(self, s):
        print('class name:', self._cls.__name__)
        return self._cls(s)


@ShowClassName
class Foobar(object):
    def __init__(self, s):
        self.value = s

    def fun(self):
        print(self.value)


a = Foobar('xieman')
a.fun()
