def wrap_class(cls):
    def inner(a):
        print('class name:', cls.__name__)
        print(a)
        return cls(a)

    return inner


@wrap_class
class Foo:
    def __init__(self, a):
        self.a = a

    def fun(self):
        print('self.a =', self.a)


m = Foo('xiaman')
m.fun()
