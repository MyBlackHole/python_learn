from threading import Timer


class RepeatingTimer(Timer):
    def run(self):
        while not self.finished.is_set():
            self.function(*self.args, **self.kwargs)
            self.finished.wait(self.interval)


class UseTimer:
    def __init__(self, interval, function_name, *args, **kwargs):
        """
        :param interval:时间间隔
        :param function_name:可调用的对象
        :param args:args和kwargs作为function_name的参数
        """
        self.timer = RepeatingTimer(interval, function_name, *args, **kwargs)

    def timer_start(self):
        self.timer.start()

    def timer_cancle(self):
        self.timer.cancel()


# 自测代码
if __name__ == "__main__":
    from time import sleep

    def hello(name, string):
        print(f"hello : {name} ,nice to : {string}")

    t = UseTimer(10, hello, ("怎料事与愿违", "不愿染是与非"))
    t.timer_start()
    sleep(10)
    t.timer_cancle()
