import time

from delay_manage import DelayManage


def timeout():
	global count
	print("timeout")
	count = 0


def long_time_task(i):
    time.sleep(i)
    print(i)


if __name__ == "__main__":
    count = 0
    while True:
        delay_manage = DelayManage()
        key = delay_manage.add(key=1, interval=1.5, function=timeout)
        delay_manage.start(key)
        long_time_task(count)
        delay_manage.cancel(key=key)
        count += 0.1
