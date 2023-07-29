import subprocess

# cmd = 'cmd.exe c:\\sam.bat'
p = subprocess.Popen(
    "cmd.exe /c" + "D:\\PycharmProjects\\python_learn\\进程\\启动bat\\1.bat abc",
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
)

curline = p.stdout.readline()
while curline != b"":
    print(curline.decode("gbk"))
    curline = p.stdout.readline()

p.wait()
print(p.returncode)
