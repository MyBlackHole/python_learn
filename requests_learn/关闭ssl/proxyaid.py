import random
from utility.zdyproxy import get_zdy_proxy


class ProxyAid(object):
    # proxy = None
    # TODO flag为False代理使用本地
    flag = False

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'proxy'):
            # setattr(cls, 'proxy', super().__new__(cls, *args, **kwargs))
            cls.proxy = super().__new__(cls, *args, **kwargs)
        return cls.proxy

    def get_proxy(self):
        proxies = None
        if self.flag:
            num = random.randint(0, 10)
            if num == 1:
                proxies = None
            else:
                proxies = get_zdy_proxy()
        return proxies


class ProxyLike(object):
    def __init__(self):
        self.flag = False

    def get_proxy(self):
        proxies = None
        if self.flag:
            num = random.randint(0, 9)
            if num == 1:
                proxies = None
            else:
                proxies = get_zdy_proxy()
        return proxies


class ProxyComment(object):

    def get_proxy(self):
        num = random.randint(0, 2)
        if num == 1:
            proxies = None
        else:
            proxies = get_zdy_proxy()
        return proxies

if __name__ == "__main__":
    p = ProxyAid()
    p1 = ProxyAid()
    print(id(p), id(p1))
    print(ProxyAid().get_proxy())
    ProxyAid().flag = True
    print(ProxyAid().flag)
    print(ProxyAid().get_proxy())
