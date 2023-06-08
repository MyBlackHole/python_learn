# coding=utf-8
import signal
import time


def set_timeout(num, callback):
    def wrap(func):
        # 收到信号 SIGALRM 后的回调函数，第一个参数是信号的数字，第二个参数是the interrupted stack frame.
        def handle(signum, frame):
            raise RuntimeError

        def to_do(*args, **kwargs):
            try:
                # 设置信号和回调函数
                signal.signal(signal.SIGALRM, handle)

                # 设置 num 秒的闹钟
                signal.alarm(num)
                print("start alarm signal.")
                r = func(*args, **kwargs)
                print("close alarm signal.")

                # 关闭闹钟
                signal.alarm(0)
                return r
            except RuntimeError as e:
                callback()

        return to_do

    return wrap


# 超时后的处理函数
def after_timeout():
    print("Time out!")


# 限时 2 秒超时
@set_timeout(2, after_timeout)
def connect():
    time.sleep(3)
    print("Finished without timeout.")


if __name__ == "__main__":
    connect()
