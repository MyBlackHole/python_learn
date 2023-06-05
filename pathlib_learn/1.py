from pathlib import Path

print(Path.cwd())
print(Path('address.txt').exists())
# file = open(Path.cwd() / 'address.txt', 'r+')
file = (Path.cwd() / 'address.txt').open('r+')
address = file.read()
file.close()
print(address)

from pathlib import Path

path = Path('.')

for p in path.rglob('*.*'):
    print(p)

print("*" * 30)

# path = Path('13_文件/2')
# path.rename(Path('13_文件/2'))
path = Path('a')
# path.rename(Path('2.txt'))

print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
print(path.parts)

# # 不存在则创建目录
# p = Path('1')
# if not p.exists():
#     p.mkdir(parents=True)

print("*" * 30)

# 获取子目录
p = Path(__file__).parent
for i in p.iterdir():
    if i.is_dir():
        print(i)
        print(len(list(i.iterdir())))
        for item in i.iterdir():
            print(int(item.stat().st_mtime))

d = {}
d[p] = 1
print(d[p])
for i in d.keys():
    print(type(i))
