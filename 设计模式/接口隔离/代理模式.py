#!/user/bin/env python
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

# 构建一个服务器，该服务器接受如下格式数据，addr代表地址，content代表接收的信息内容
info_struct = dict()
info_struct["addr"] = 10000
info_struct["content"] = ""


class Server(metaclass=ABCMeta):
    def __init__(self):
        self.content = ""

    @abstractmethod
    def recv(self, info):
        pass

    @abstractmethod
    def send(self, info):
        pass

    @abstractmethod
    def show(self):
        pass


class InfoServer(Server):
    def recv(self, info):
        self.content = info
        return "recv OK!"

    def send(self, info):
        pass

    def show(self):
        print("SHOW:%s" % self.content)


"""
infoServer有接收和发送的功能，发送功能由于暂时用不到，保留。
另外新加一个接口show，用来展示服务器接收的内容。
接收的数据格式必须如info_struct所示，服务器仅接受info_struct的content字段。
那么，如何给这个服务器设置一个白名单，使得只有白名单里的地址可以访问服务器呢？
修改Server结构是个方法，但这显然不符合软件设计原则中的单一职责原则。
在此基础之上，使用代理，是个不错的方法。代理配置如下
"""


class ServerProxy:
    @abstractmethod
    def __init__(self):
        self.server = ""


class InfoServerProxy(ServerProxy):

    def __init__(self, server):
        super().__init__()
        self.server = server

    def recv(self, info):
        return self.server.recv(info)

    def show(self):
        self.server.show()


class WhiteInfoServerProxy(InfoServerProxy):
    white_list = []

    def recv(self, info):
        try:
            assert type(info) == dict
        except Exception as e:
            print(e)
            return "info structure is not correct"
        addr = info.get("addr", 0)
        if addr not in self.white_list:
            return "Your address is not in the white list."
        else:
            content = info.get("content", "")
            return self.server.recv(content)

    def add_white(self, addr):
        self.white_list.append(addr)

    def rmv_white(self, addr):
        self.white_list.remove(addr)

    def clear_white(self):
        self.white_list = []


if __name__ == "__main__":
    info_struct = dict()
    info_struct["addr"] = 10010
    info_struct["content"] = "Hello World!"
    info_server = InfoServer()
    info_server_proxy = WhiteInfoServerProxy(info_server)
    print(info_server_proxy.recv(info_struct))
    info_server_proxy.show()
    info_server_proxy.add_white(10010)
    print(info_server_proxy.recv(info_struct))
    info_server_proxy.show()
