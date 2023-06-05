# a = ("a", "b")
# print(type(a))
# print("woxiang %s" % a)
# # 运行结果：
# # print('woxiang %s' % a)

# TypeError: not all arguments converted during string formatting

# 首先定义了一个变量a，变量a的格式为<class 'tuple'>
# 原字符串‘woxiang’后想添加变量生成一个新的字符串，很显然，元组是有两个元素，
# 占位符%s只占了一个位置，另一个元素无处安放了，因此报错。那么，这个问题怎么解决呢？
# 显然，有多少个元素，就放几个占位符%s即可，中间以，隔开即可
a = ("a", "b")
print(type(a))
print("woxiang %s%s" % a)

# 运行结果：
# <class 'tuple'>
# woxiang ab
# 那，如果是三个或者四个元素的元组呢？很显然，有几个元素，放几个占位符
# 也就是n个元素放n个占位符
b = ("aa", "cc", "dd")
print("woxiang %s,%s,%s" % b)
# 运行结果：
# woxiang aa,cc,dd
