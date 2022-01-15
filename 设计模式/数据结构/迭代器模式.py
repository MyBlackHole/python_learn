#!/user/bin/env python
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

"""
大话设计模式
设计模式——迭代器模式
迭代器模式(Iterator Pattern):提供方法顺序访问一个聚合对象中各元素，而又不暴露该对象的内部表示.
"""


# 迭代器抽象类
class Iterator(object):
    @abstractmethod
    def first(self):
        pass

    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def is_done(self):
        pass

    @abstractmethod
    def curr_item(self):
        pass


# 聚集抽象类
class Aggregate(metaclass=ABCMeta):

    @abstractmethod
    def create_iterator(self):
        pass


# 具体迭代器类
class ConcreteIterator(Iterator):

    def __init__(self, aggregate):
        self.aggregate = aggregate
        self.curr = 0

    def first(self):
        return self.aggregate[0]

    def next(self):
        ret = None
        self.curr += 1
        if self.curr < len(self.aggregate):
            ret = self.aggregate[self.curr]
        return ret

    def is_done(self):
        return True if self.curr + 1 >= len(self.aggregate) else False

    def curr_item(self):
        return self.aggregate[self.curr]


# 具体聚集类
class ConcreteAggregate(Aggregate):

    def __init__(self):
        self.lists = []

    def create_iterator(self):
        return ConcreteIterator(self)


class ConcreteIteratorDesc(Iterator):
    def __init__(self, aggregate):
        self.aggregate = aggregate
        self.curr = len(aggregate) - 1

    def first(self):
        return self.aggregate[-1]

    def next(self):
        ret = None
        self.curr -= 1
        if self.curr >= 0:
            ret = self.aggregate[self.curr]
        return ret

    def is_done(self):
        return True if self.curr - 1 < 0 else False

    def curr_item(self):
        return self.aggregate[self.curr]


if __name__ == "__main__":
    ca = ConcreteAggregate()
    ca.lists.append("大鸟")
    ca.lists.append("小菜")
    ca.lists.append("老外")
    ca.lists.append("小偷")

    it = ConcreteIterator(ca.lists)
    print(it.first())
    while not it.is_done():
        print(it.next())
    print("————倒序————")
    itd = ConcreteIteratorDesc(ca.lists)
    print(itd.first())
    while not itd.is_done():
        print(itd.next())
