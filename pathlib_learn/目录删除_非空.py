from pathlib import Path

p = Path("1")
dirlist = [i for i in p.iterdir() if i.is_dir()]
print(dirlist)
for i in dirlist:
    try:
        i.rmdir()
    except:
        print(str(i) + " 不为空")
