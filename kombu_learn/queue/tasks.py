import time


def hello_task(who="world"):
    print(f"Start Hello {who}")
    print(f"sleep")
    time.sleep(10)
    print(f"End Hello {who}")
