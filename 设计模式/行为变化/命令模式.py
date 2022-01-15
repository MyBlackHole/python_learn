#!/user/bin/env python
# -*- coding: utf-8 -*-
from abc import abstractmethod


# 主食子系统，凉菜子系统，热菜子系统,后台三个子系统
class BackSys:
    @abstractmethod
    def cook(self, ds):
        pass


class MainFoodSys(BackSys):
    def cook(self, ds):
        print("MAINFOOD:Cook %s" % ds)


class CoolDishSys(BackSys):
    def cook(self, ds):
        print("COOLDISH:Cook %s" % ds)


class HotDishSys(BackSys):
    def cook(self, ds):
        print("HOTDISH:Cook %s" % ds)


# 前台服务员系统与后台系统的交互，我们可以通过命令的模式来实现，
# 服务员将顾客的点单内容封装成命令，直接对后台下达命令，后台完成命令要求的事，

# 前台系统构建如下
class WaiterSys:
    menu_map = dict()
    commandList = []

    def set_order(self, command):
        print("WAITER:Add dish")
        self.commandList.append(command)

    def cancel_order(self, command):
        print("WAITER:Cancel order...")
        self.commandList.remove(command)

    def notify(self):
        print("WAITER:Notify...")
        for command in self.commandList:
            command.execute()


# 前台系统中的notify接口直接调用命令中的execute接口，执行命令。命令类构建
class Command:

    def __init__(self, receiver=None):
        self.receiver = receiver

    @abstractmethod
    def execute(self):
        pass


class FoodCommand(Command):

    def __init__(self, receiver, ds=""):
        super().__init__()
        self.receiver = receiver
        self.ds = ds

    def execute(self):
        self.receiver.cook(self.ds)


class MainFoodCommand(FoodCommand):
    pass


class CoolDishCommand(FoodCommand):
    pass


class HotDishCommand(FoodCommand):
    pass


"""
Command类是个比较通过的类，foodCommand类是本例中涉及的类，相比于Command类进行了一定的改造。
由于后台系统中的执行函数都是cook，因而在foodCommand类中直接将execute接口实现，
如果后台系统执行函数不同，需要在三个子命令系统中实现execute接口。
这样，后台三个命令类就可以直接继承，不用进行修改了。
"""


# 菜单类辅助业务
class MenuAll:
    menu_map = dict()

    def load_menu(self):  # 加载菜单，这里直接写死
        self.menu_map["hot"] = ["Yu-Shiang Shredded Pork", "Sauteed Tofu, Home Style", "Sauteed Snow Peas"]
        self.menu_map["cool"] = ["Cucumber", "Preserved egg"]
        self.menu_map["main"] = ["Rice", "Pie"]

    def is_hot(self, ds):
        if ds in self.menu_map["hot"]:
            return True
        return False

    def is_cool(self, ds):
        if ds in self.menu_map["cool"]:
            return True
        return False

    def is_main(self, ds):
        if ds in self.menu_map["main"]:
            return True
        return False


# 业务场景
if __name__ == "__main__":
    dish_list = ["Yu-Shiang Shredded Pork", "Sauteed Tofu, Home Style", "Cucumber", "Rice"]  # 顾客点的菜
    waiter_sys = WaiterSys()
    main_food_sys = MainFoodSys()
    cool_dish_sys = CoolDishSys()
    hot_dish_sys = HotDishSys()
    menu = MenuAll()
    menu.load_menu()
    for dish in dish_list:
        if menu.is_cool(dish):
            cmd = CoolDishCommand(cool_dish_sys, dish)
        elif menu.is_hot(dish):
            cmd = HotDishCommand(hot_dish_sys, dish)
        elif menu.is_main(dish):
            cmd = MainFoodCommand(main_food_sys, dish)
        else:
            continue
        waiter_sys.set_order(cmd)
    waiter_sys.notify()
