#!/usr/bin/env python
# coding: utf-8
# yc@2013/04/28

import subprocess


def test(size):
    print("start")

    cmd = "dd if=/dev/urandom bs=1 count=%d 2>/dev/null" % size
    p = subprocess.Popen(
        args=cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        close_fds=True,
    )

    # if p.stdout is not None:
    #     for raw_line in iter(p.stdout.readline, b""):
    #         line = raw_line.decode("utf-8", errors="backslashreplace").rstrip()
    #         print("%s", line)

    # p.communicate()

    # 堵塞 cmd 运行, 需要读出数据才能继续下去
    p.wait()  # 这里超出管道限制，将会卡住子进程

    print("end")


# 64KB
test(64 * 1024)

# 64KB + 1B
test(64 * 1024 + 1)

# # output :
# start
# end
# start  #  然后就阻塞了。
