# 普通装饰器（装饰函数和类）
def deco111(func_or_cls):
    def wrap(*args, **kwargs):
        print(type(func_or_cls))
        return func_or_cls(*args, **kwargs)

    return wrap


# 装饰器中的self关键字使用（动态访问类中的其他方法/属性）
def deco222(func_or_cls):
    print("---")

    def wrap(self, *args, **kwargs):  # self 关键字专门接收类或实例对象
        print(type(func_or_cls))
        if func_or_cls.__name__ == "x4":
            if hasattr(self, "x1"):
                self.x1()  # 动态调用类中的方法
                print(self.a)  # 以及属性
                return func_or_cls(self, *args, **kwargs)

        return func_or_cls(self, *args, **kwargs)

    return wrap


class X:
    a = 666

    @classmethod
    @deco111
    def x1(self):
        print(333)

    @deco111
    @classmethod
    def x2(cls):
        print(123)

    @deco111
    @staticmethod  # 如果要对静态方法和类方法进行装饰，
    # 要将@staticmethod或classmethod的帽子戴在最上面，装饰器的执行是从下到上的
    def x3(self):
        print(456)

    @classmethod
    @deco222  # 使用第二个装饰器
    def x4(self):
        print(789)


# X.x1() #正常
# X.x2() #异常 'classmethod' object is not callable
# X.x3() #异常 'staticmethod' object is not callable
# X().x4() #正常


def get_parameter(
    *args, **kwargs
):  # 工厂函数，用来接受@get_parameter('index.html/')的'index.html/'
    print(1)

    def log_time(func):
        print(2)

        def make_decorater(name):
            print(args, kwargs)
            print("现在开始装饰")
            print(name)
            func()
            print("现在结束装饰")

        print(3)
        return make_decorater

    return log_time


@get_parameter("index.html/")
def test():
    print("我是被装饰的函数")
    # return num+1


test(1)  # test()=make_decorater()
