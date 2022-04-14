import os
from tempfile import TemporaryFile

# 1. 读取
f = TemporaryFile(mode="w+b", dir="/tmp/test")
#   参数：
#       1). mode="w+"   允许 打开的模式， 默认 为 w+b 模式
#           w     写模式
#           w+    读写模式
#           w+b   读写 Bytes 模式
#       2). buffering=-1     缓冲区大小， -1 是不限制
#       3). encoding=None    读取的文件的字符编码
f.write(b"abcdefg\nhijkmlm\nopqist\nuvwxyz")  # 写入
f.seek(0)  # 将 光标 切换到开始

# line = f.readlines()  # 按照 每一行进行读取
# line = f.read()  # 读取全部
# print(line)
# print(dir(f))
print(f)
fa = open(f.name)
text = fa.read()
print(text)
print(os.path.exists(f"/tmp/test/fskdjf"))
