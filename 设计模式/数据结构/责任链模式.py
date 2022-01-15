#!/user/bin/env python
# -*- coding: utf-8 -*-
from abc import abstractmethod


# 构造抽象经理类和各个层级的经理类：
class Manager:

    def __init__(self, name=""):
        self.successor = None
        self.name = name

    def set_successor(self, successor):
        self.successor = successor

    @abstractmethod
    def handle_request(self, rq):
        pass


class LineManager(Manager):
    def handle_request(self, rq):
        if rq.requestType == 'DaysOff' and rq.number <= 3:
            print('%s:%s Num:%d Accepted OVER' % (self.name, rq.requestContent, rq.number))
        else:
            print('%s:%s Num:%d Accepted CONTINUE' % (self.name, rq.requestContent, rq.number))
            if self.successor is not None:
                self.successor.handle_request(rq)


class DepartmentManager(Manager):
    def handle_request(self, rq):
        if rq.requestType == 'DaysOff' and rq.number <= 7:
            print('%s:%s Num:%d Accepted OVER' % (self.name, rq.requestContent, rq.number))
        else:
            print('%s:%s Num:%d Accepted CONTINUE' % (self.name, rq.requestContent, rq.number))
            if self.successor is not None:
                self.successor.handle_request(rq)


class GeneralManager(Manager):
    def handle_request(self, rq):
        if rq.requestType == 'DaysOff':
            print('%s:%s Num:%d Accepted OVER' % (self.name, rq.requestContent, rq.number))


class Request:
    def __init__(self):
        self.requestType = ''
        self.requestContent = ''
        self.number = 0


# request类封装了假期请求。在具体的经理类中，可以通过setSuccessor接口来构建“责任链”，并在handleRequest接口中实现逻辑。
# 场景类中实现如下
if __name__ == "__main__":
    line_manager = LineManager('LINE MANAGER')
    department_manager = DepartmentManager('DEPARTMENT MANAGER')
    general_manager = GeneralManager('GENERAL MANAGER')

    line_manager.set_successor(department_manager)
    department_manager.set_successor(general_manager)

    req = Request()
    req.requestType = 'DaysOff'
    req.requestContent = 'Ask 1 day off'
    req.number = 1
    line_manager.handle_request(req)

    req.requestType = 'DaysOff'
    req.requestContent = 'Ask 5 days off'
    req.number = 5
    line_manager.handle_request(req)

    req.requestType = 'DaysOff'
    req.requestContent = 'Ask 10 days off'
    req.number = 10
    line_manager.handle_request(req)
