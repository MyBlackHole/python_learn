#!/usr/bin/env python
# -*- coding: utf-8 -*-

import signal
import time
from contextlib import contextmanager
from threading import Thread


class TimeoutException(Exception):
    pass


@contextmanager
def time_limit(seconds, func):
    def signal_handler(signum, frame):
        raise TimeoutException("Timed out!")

    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        func("time_limit")
        yield
    finally:
        signal.alarm(0)


def long_function_call(count):
    time.sleep(count)
    print("ok")


def test():
    try:
        count = 1
        while count:
            with time_limit(5, print):
                long_function_call(count)
            count += 2
    except TimeoutException as e:
        print(e)


def test1():
    while True:
        print("test1")
        time.sleep(1)


if __name__ == "__main__":
    Thread(target=test).start()
    Thread(target=test1).start()
