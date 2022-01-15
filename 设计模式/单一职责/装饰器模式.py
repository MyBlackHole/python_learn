#!/user/bin/env python
# -*- coding: utf-8 -*-
from abc import abstractmethod, ABCMeta


# 又提到了那个快餐点餐系统，不过今天我们只以其中的一个类作为主角：饮料类。首先，回忆下饮料类：
class Beverage(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        self.name = ""
        self.price = 0.0
        self.type = "BEVERAGE"

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_name(self):
        return self.name


class Coke(Beverage):
    def __init__(self):
        super().__init__()
        self.name = "coke"
        self.price = 4.0


class Milk(Beverage):
    def __init__(self):
        super().__init__()
        self.name = "milk"
        self.price = 5.0


# 除了基本配置，快餐店卖可乐时，可以选择加冰，如果加冰的话，要在原价上加0.3元；
# 卖牛奶时，可以选择加糖，如果加糖的话，要原价上加0.5元。怎么解决这样的问题？
# 可以选择装饰器模式来解决这一类的问题。首先，定义装饰器类：
class DrinkDecorator(metaclass=ABCMeta):
    """
    商品抽象类
    """

    @abstractmethod
    def get_name(self):
        """
        获取商品名称抽象方法
        """

    @abstractmethod
    def get_price(self):
        """
        获取商品名称抽象方法
        """


class IceDecorator(DrinkDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def get_name(self):
        return self.beverage.get_name() + " + ice"

    def get_price(self):
        return self.beverage.get_price() + 0.3


class SugarDecorator(DrinkDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def get_name(self):
        return self.beverage.getName() + " + sugar"

    def get_price(self):
        return self.beverage.getPrice() + 0.5


# 构建好装饰器后，在具体的业务场景中，就可以与饮料类进行关联。以可乐+冰为例，示例业务场景如下：
if __name__ == "__main__":
    coke_cola = Coke()
    print("Name:%s" % coke_cola.get_name())
    print("Price:%s" % coke_cola.get_price())
    ice_coke = IceDecorator(coke_cola)
    print("Name:%s" % ice_coke.get_name())
    print("Price:%s" % ice_coke.get_price())
