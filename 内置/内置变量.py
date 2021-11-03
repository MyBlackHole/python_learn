"""
获取注释1
"""
# 只获得最前的注释
print(__doc__)

# 当前文件路径
from pathlib import Path

print(Path(__file__).parent)
print(Path(__file__).name)

# .py文件所在文件夹
print(__package__)

# 模块名
print(__name__)

for i in dir(__builtins__):
    print(i)
print(__file__)
