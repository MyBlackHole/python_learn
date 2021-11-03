#!/user/bin/env python
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, action):
        pass


class AlarmSensor(Observer):
    def update(self, action):
        print("Alarm Got: %s" % action)
        print("Alarm Ring...")


class WaterSk(Observer):
    def update(self, action):
        print("Sk Got: %s" % action)
        print("Spray Water...")


class EmergencyDialer(Observer):
    def update(self, action):
        print("Dialer Got: %s" % action)
        print("Dial 119...")


"""
观察者中定义了update接口，如果被观察者状态比较多，或者每个具体的观察者方法比较多，可以通过update传参数进行更丰富的控制。
下面构造被观察者。
"""


class Observed:
    def __init__(self):
        self.observers = []
        self.action = ""

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_all(self):
        for obs in self.observers:
            obs.update(self.action)


class SmokeSensor(Observed):
    def set_action(self, action):
        self.action = action


"""
被观察者中首先将观察对象加入到观察者数组中，若发生情况，则通过notifyAll通知各观察者。
业务代码如下：
"""

if __name__ == "__main__":
    alarm = AlarmSensor()
    sk = WaterSk()
    dialer = EmergencyDialer()

    smoke_sensor = SmokeSensor()
    smoke_sensor.add_observer(alarm)
    smoke_sensor.add_observer(sk)
    smoke_sensor.add_observer(dialer)

    smoke_sensor.set_action("On Fire!")
    smoke_sensor.notify_all()
