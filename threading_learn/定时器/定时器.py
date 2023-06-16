import time
from threading import Timer

status = False

a = True


def stop_status():
    while a:
        global status
        status = True


def test():
    print("test")
    return "ok"


t = None
count = 0
while count < 8:
    if t:
        t.cancel()
    t = Timer(4, test, [])
    t.start()
    print("while")
    time.sleep(count)
    count += 1
