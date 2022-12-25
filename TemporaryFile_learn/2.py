import os
from tempfile import NamedTemporaryFile

# 1. 读取
f = NamedTemporaryFile(mode="w+", dir=r"/tmp/")
#   参数：
#       1). mode="w+"   允许 打开的模式， 默认 为 w+b 模式
#           w     写模式
#           w+    读写模式
#           w+b   读写 Bytes 模式
#       2). buffering=-1      缓冲区大小， -1 是不限制
#       3). encoding=None     读取的文件的字符编码
#       4). dir=None          临时文件存放的文件的位置
#       5). delete=True       变量删除后 将文件删除, delete=False 时，变量删除时不会删除
print(f.name)  # 打印文件名
print(os.path.exists(f.name))
f.write("abcdefg\nhijkmlm\nopqist\nuvwxyz")  # 写入
f.seek(0)  # 将 光标 切换到开始
# line = f.readlines()  # 按照 每一行进行读取
line = f.read()  # 读取全部
print(line)
