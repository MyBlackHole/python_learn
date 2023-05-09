import threading
import time


class PeriodicTimer:
    def __init__(self, interval):
        self._interval = interval
        self._flag = 0
        self._cv = threading.Condition()

    def start(self):
        t = threading.Thread(target=self.run)
        t.daemon = True

        t.start()

    def run(self):
        """
        运行计时器并在每个间隔后通知等待线程
        """
        while True:
            time.sleep(self._interval)
            with self._cv:
                # ^进行位运算
                self._flag ^= 1
                # notify通知
                self._cv.notify_all()

    def wait_for_tick(self):
        """
        等待计时器的下一个滴答
        """
        with self._cv:
            last_flag = self._flag
            while last_flag == self._flag:
                # wait等待
                self._cv.wait()


# 计时器的使用示例
ptimer = PeriodicTimer(5)
ptimer.start()


# 两个在计时器上同步的线程
def countdown(nticks):
    while nticks > 0:
        ptimer.wait_for_tick()
        print("T-minus", nticks)
        nticks -= 1


def countup(last):
    n = 0
    while n < last:
        ptimer.wait_for_tick()
        print("Counting", n)
        n += 1


threading.Thread(target=countdown, args=(10,)).start()
threading.Thread(target=countup, args=(5,)).start()
