#!/user/bin/env python
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

# 使用前
"""
class StockQueryDevice(metaclass=ABCMeta):
    def __init__(self):
        self.stock_code = "0"
        self.stock_price = 0.0

    @abstractmethod
    def login(self, usr, pwd):
        pass

    def set_code(self, code):
        self.stock_code = code

    @abstractmethod
    def query_price(self):
        pass

    @abstractmethod
    def show_price(self):
        pass


class WebAStockQueryDevice(StockQueryDevice):

    def login(self, usr, pwd):
        if usr == "myStockA" and pwd == "myPwdA":
            print("Web A:Login OK... user:%s pwd:%s" % (usr, pwd))
            return True
        else:
            print("Web A:Login ERROR... user:%s pwd:%s" % (usr, pwd))
            return False

    def query_price(self):
        print("Web A Querying...code:%s " % self.stock_code)
        self.stock_price = 20.00

    def show_price(self):
        print("Web A Stock Price...code:%s price:%s" % (self.stock_code, self.stock_price))


if __name__ == "__main__":
    web_a_query_dev = WebAStockQueryDevice()
    web_a_query_dev.login("myStockA", "myPwdA")
    web_a_query_dev.set_code("12345")
    web_a_query_dev.query_price()
    web_a_query_dev.show_price()
"""


# 后
class StockQueryDevice(metaclass=ABCMeta):
    def __init__(self):
        self.stock_code = "0"
        self.stock_price = 0.0

    @abstractmethod
    def login(self, usr, pwd):
        pass

    def set_code(self, code):
        self.stock_code = code

    @abstractmethod
    def query_price(self):
        pass

    @abstractmethod
    def show_price(self):
        pass

    def operate_query(self, usr, pwd, code):
        if not self.login(usr, pwd):
            return False
        self.set_code(code)
        self.query_price()
        self.show_price()
        return True


class WebBStockQueryDevice(StockQueryDevice):
    def login(self, usr, pwd):
        if usr == "myStockB" and pwd == "myPwdB":
            print("Web B:Login OK... user:%s pwd:%s" % (usr, pwd))
            return True
        else:
            print("Web B:Login ERROR... user:%s pwd:%s" % (usr, pwd))
            return False

    def query_price(self):
        print("Web B Querying...code:%s " % self.stock_code)
        self.stock_price = 30.00

    def show_price(self):
        print("Web B Stock Price...code:%s price:%s" % (self.stock_code, self.stock_price))


if __name__ == "__main__":
    web_a_query_dev = WebBStockQueryDevice()
    web_a_query_dev.operate_query("myStockA", "myPwdA", "12345")
