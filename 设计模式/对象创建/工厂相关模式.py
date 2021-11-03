#!/user/bin/env python
# -*- coding: utf-8 -*-

from abc import abstractmethod, ABCMeta


class Creator(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        self.name = ""
        self.price = 0.0
        self.type = ''

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_name(self):
        return self.name


class CheeseBurger(Creator):
    def __init__(self):
        super().__init__()
        self.name = "cheese burger"
        self.price = 10.0


class SpicyChickenBurger(Creator):
    def __init__(self):
        super().__init__()
        self.name = "spicy chicken burger"
        self.price = 15.0


class Chips(Creator):
    def __init__(self):
        super().__init__()
        self.name = "chips"
        self.price = 6.0


class ChickenWings(Creator):
    def __init__(self):
        super().__init__()
        self.name = "chicken wings"
        self.price = 12.0


class Coke(Creator):
    def __init__(self):
        super().__init__()
        self.name = "coke"
        self.price = 4.0


class Milk(Creator):
    def __init__(self):
        super().__init__()
        self.name = "milk"
        self.price = 5.0


class FoodFactory:
    """
    抽象工厂foodFactory为抽象的工厂类，而burgerFactory，snackFactory，beverageFactory为具体的工厂类。
    """

    @abstractmethod
    def __init__(self):
        self.type = ""

    def create_food(self, foodClass):
        print(self.type, " factory produce a instance.")
        foodIns = foodClass()
        return foodIns


class BurgerFactory(FoodFactory):
    def __init__(self):
        super().__init__()
        self.type = "BURGER"


class SnackFactory(FoodFactory):
    def __init__(self):
        super().__init__()
        self.type = "SNACK"


class BeverageFactory(FoodFactory):
    def __init__(self):
        super().__init__()
        self.type = "BEVERAGE"


if __name__ == "__main__":
    Burger_factory = BurgerFactory()
    Snack_factory = SnackFactory()
    Beverage_factory = BeverageFactory()
    Cheese_burger = Burger_factory.create_food(CheeseBurger)
    print(Cheese_burger.get_name(), Cheese_burger.get_price())
    chicken_wings = Snack_factory.create_food(ChickenWings)
    print(chicken_wings.get_name(), chicken_wings.get_price())
    coke_drink = Beverage_factory.create_food(Coke)
    print(coke_drink.get_name(), coke_drink.get_price())
