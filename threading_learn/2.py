from threading import Thread
import time

i = 0
i_bat = 0

def func():
    global i
    for _ in range(10000):
        global i_bat
        i_bat = 0
        time.sleep(0.0001)
        i_bat = 1
        time.sleep(0.0001)
        i = i + i_bat


t_list = []
for j in range(2):
    t1 = Thread(target=func)
    t_list.append(t1)
    t1.start()

for t in t_list:
    t.join()
print(i)
