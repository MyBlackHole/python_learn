#!/user/bin/env python
# -*- coding: utf-8 -*-


# 假设有一个网上咖啡选购平台，客户可以在该平台上下订单订购咖啡，平台会根据用户位置进行线下配送。
# 假设其咖啡对象构造如下：
class Coffee:
    def __index__(self):
        self.name = ''
        self.price = 0

    def __init__(self, name):
        self.name = name
        self.price = len(name)  # 在实际业务中，咖啡价格应该是由配置表进行配置，或者调用接口获取等方式得到，此处为说明享元模式，将咖啡价格定为名称长度，只是一种简化

    def show(self):
        print("Coffee Name:%s Price:%s" % (self.name, self.price))


class CoffeeFactory:
    def __init__(self):
        self.coffee_dict = {}

    def get_coffee(self, name):
        if not self.coffee_dict.__contains__(name):
            self.coffee_dict[name] = Coffee(name)
        return self.coffee_dict[name]

    def get_coffee_count(self):
        return len(self.coffee_dict)


# 咖啡工厂中，getCoffeeCount直接返回当前实例个数。重写后的Customer
class Customer:
    def __index__(self):
        self.coffee_ft = ""
        self.name = ""

    def __init__(self, name, coffee_ft):
        self.name = name
        self.coffee_ft = coffee_ft

    def order(self, coffee_name):
        print("%s ordered a cup of coffee:%s" % (self.name, coffee_name))
        return self.coffee_ft.get_coffee(coffee_name)


# 假设业务中短时间内有多人订了咖啡，业务模拟如下
if __name__ == "__main__":
    coffee_factory = CoffeeFactory()
    customer_1 = Customer("A Client", coffee_factory)
    customer_2 = Customer("B Client", coffee_factory)
    customer_3 = Customer("C Client", coffee_factory)
    c1_app = customer_1.order("cappuccino")
    c1_app.show()
    c2_mocha = customer_2.order("mocha")
    c2_mocha.show()
    c3_app = customer_3.order("cappuccino")
    c3_app.show()
    print("Num of Coffee Instance:%s" % coffee_factory.get_coffee_count())
