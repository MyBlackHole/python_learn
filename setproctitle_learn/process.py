import time
import setproctitle

# 获取当前进程名
# Windows可能有问题
proc_title = setproctitle.getproctitle()
print(proc_title)

# 重命名进程名
proc_title = "new_proc_title"
setproctitle.setproctitle(proc_title)
proc_title = setproctitle.getproctitle()
print(proc_title)

time.sleep(100)
