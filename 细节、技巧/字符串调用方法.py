# # eval()
# def foo():
#     print('foo')
#
#
# def bar():
#     print('bar')
#
#
# func_list = ['foo', 'bar']
#
# for i in func_list:
#     eval(i)()

# locals()和globals()
def foo():
    print('foo')


def bar():
    print('bar')


func_list = ['foo', 'bar']

for func in func_list:
    locals()[func]()

for func in func_list:
    globals()[func]()

print(locals())


# getattr()
class Foo:
    def do_foo(self):
        print(" {} ".format(self))

    def do_bar(self):
        print("do_bar")


f = getattr(Foo(), 'do_' + "bar")
f()
