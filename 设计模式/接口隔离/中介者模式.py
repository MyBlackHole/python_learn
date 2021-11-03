#!/user/bin/env python
# -*- coding: utf-8 -*-
# 路由系统；著名的MVC框架中，其中的C（Controller）就是M（Model）和V（View）的中介者。

# 构造三个子系统，即三个类（在中介者模式中，这些类叫做同事类）
class Colleague:
    def __init__(self, mediator):
        self.mediator = mediator


class PurchaseColleague(Colleague):
    def buy_stuff(self, num):
        print("PURCHASE:Bought %s" % num)
        self.mediator.execute("buy", num)

    def get_notice(self, num):
        print(num)


class WarehouseColleague(Colleague):
    total = 0
    threshold = 100

    def set_threshold(self, threshold):  # 设置阈值
        self.threshold = threshold

    def is_enough(self):
        if self.total < self.threshold:
            print("WAREHOUSE:Warning...Stock is low... ")
            self.mediator.execute("warning", self.total)
            return False
        else:
            return True

    def inc(self, num):
        self.total += num
        print("WAREHOUSE:Increase %s" % num)
        self.mediator.execute("increase", num)
        self.is_enough()

    def dec(self, num):
        if num > self.total:
            print("WAREHOUSE:Error...Stock is not enough")
        else:
            self.total -= num
            print("WAREHOUSE:Decrease %s" % num)
            self.mediator.execute("decrease", num)
        self.is_enough()


class SalesColleague(Colleague):
    def sell_stuff(self, num):
        print("SALES:Sell %s" % num)
        self.mediator.execute("sell", num)

    def get_notice(self, num):
        print(num)


# 当各个类在初始时都会指定一个中介者，而各个类在有变动时，也会通知中介者，由中介者协调各个类的操作。
# 中介者实现
class AbstractMediator():
    purchase = ""
    sales = ""
    warehouse = ""

    def set_purchase(self, purchase):
        self.purchase = purchase

    def set_warehouse(self, warehouse):
        self.warehouse = warehouse

    def set_sales(self, sales):
        self.sales = sales

    def execute(self, content, num):
        pass


class StockMediator(AbstractMediator):
    def execute(self, content, num):
        print("MEDIATOR:Get Info--%s" % content)
        if content == "buy":
            self.warehouse.inc(num)
            self.sales.get_notice("Bought %s" % num)
        elif content == "increase":
            self.sales.get_notice("Inc %s" % num)
            self.purchase.get_notice("Inc %s" % num)
        elif content == "decrease":
            self.sales.get_notice("Dec %s" % num)
            self.purchase.get_notice("Dec %s" % num)
        elif content == "warning":
            self.sales.get_notice("Stock is low.%s Left." % num)
            self.purchase.get_notice("Stock is low. Please Buy More!!! %s Left" % num)
        elif content == "sell":
            self.warehouse.dec(num)
            self.purchase.get_notice("Sold %s" % num)
        else:
            pass


# 中介者模式中的execute是最重要的方法，它根据同事类传递的信息，直接协调各个同事的工作。
# 在场景类中，设置仓储阈值为200，先采购300，再卖出120，实现如下
if __name__ == "__main__":
    mobile_mediator = StockMediator()  # 先配置
    mobile_purchase = PurchaseColleague(mobile_mediator)
    mobile_warehouse = WarehouseColleague(mobile_mediator)
    mobile_sales = SalesColleague(mobile_mediator)
    mobile_mediator.set_purchase(mobile_purchase)
    mobile_mediator.set_warehouse(mobile_warehouse)
    mobile_mediator.set_sales(mobile_sales)

    mobile_warehouse.set_threshold(200)
    mobile_purchase.buy_stuff(300)
    mobile_sales.sell_stuff(120)
