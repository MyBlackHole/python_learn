# import os
#
# host_dict = {}
# for parent, dirnames, filenames in os.walk('.', followlinks=True):
#     print('parent: ', parent)
#     print('dirnames: ', dirnames)
#     print('filenames: ', filenames)
"""
parent:  .
dirnames:  ['13_文件', '2']
filenames:  ['test1.py', '遍历文件与目录.py']
parent:  .\13_文件
dirnames:  ['1']
filenames:  ['hm_01_读取文件.py', 'hm_02_读取文件后文件指针会改变.py', 'hm_03_写入文件.py', 'hm_04_分行读取文件.py', 'hm_05_复制文件.py', 'hm_06_复制大文件.py', 'hm_07_python2字符串.py', 'hm_08_eval计算器.py', 'README']
parent:  .\13_文件\1
dirnames:  []
filenames:  ['REAMDE[复件]']
parent:  .\2
dirnames:  []
filenames:  []
"""

from pathlib import Path

import arrow

print(arrow.now().shift(days=-10).timestamp, '\n')
path = Path()
# print(path.resolve())
for item in path.rglob('*.py'):
    print(item, int(item.stat().st_mtime))
