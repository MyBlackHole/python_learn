from threading import Timer
from threading import Lock


class DelayManage(object):
    delay_mange = None

    def __new__(cls):
        if cls.delay_mange is None:
            cls.delay_mange = object.__new__(cls)
        return cls.delay_mange

    def __init__(self, max=None) -> None:
        super().__init__()
        self.timer_dict: dict = {}
        self.max = max
        self.len = 0
        self.local = Lock()

    def add(self, key, interval, function, args=None, kwargs=None):
        self.local.acquire()
        self.timer_dict[key] = Timer(
            interval=interval,
            function=function,
            args=args,
            kwargs=kwargs)
        self.local.release()
        return key

    def delete(self, key):
        self.local.acquire()

        # 确保被取消
        self.cancel(key)
        self.timer_dict.pop(key)
        self.local.release()
        return True

    def start(self, key):
        timer = self.exist(key)
        if timer:
            timer.start()
            return True
        else:
            return False

    def exist(self, key):
        return self.timer_dict.get(key)

    def cancel(self, key):
        timer = self.exist(key)
        if timer:
            timer.cancel()
            return True
        else:
            return False
