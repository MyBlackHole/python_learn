# -*- coding: utf-8 -*-
import logging
import os
import time

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s",
    datefmt="%a, %d %b %Y %H:%M:%S",
    filename="./demo.log",
    filemode="a",
)


# Demo.py 10秒关闭程序，模拟程序崩溃
# author 胖胖的alex 2017/09/10
def execute():
    pid = str(os.getpid())
    logging.info(f"启动程序，进程号：{pid}")
    i = 1
    while True:
        # logging.info(f'pid = {pid} ---------- run{str(i)}s ')
        time.sleep(1)
        print(i)
        i += 1
        if i > 200:
            break
    logging.info("程序关闭...")


if __name__ == "__main__":
    execute()
