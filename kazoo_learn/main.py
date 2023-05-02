# coding=utf-8
import time

from kazoo.client import KazooClient

zk = KazooClient(hosts="172.17.0.2:2181")
zk.start()

# @zk.DataWatch("/")
# def my_func(data, stat, event):
#     print("Data is %s" % data)
#     print("Version is %s" % stat.version)
#     # print("Event is %s" % event)
#     print("\n")


# s = set()


@zk.ChildrenWatch("/")
def my_child(childs):
    print(childs)
    # for child in childs:
    #     if child is s:
    #         continue


while True:
    zk.DataWatch("/")
    time.sleep(10)
    print("ok")
