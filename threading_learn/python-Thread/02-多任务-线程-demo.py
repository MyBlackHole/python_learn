import threading
import time


def sing():
    """唱歌 5秒钟"""
    for i in range(5):
        print("----正在唱:菊花茶----")
        time.sleep(1)


def dance():
    """跳舞 5秒钟"""
    for i in range(5):
        print("----正在跳舞----")
        time.sleep(1)

def stop_threading(t_list: list[threading.Thread]):
    for t in t_list:
        t.


def main():
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()
    t1 = threading.Thread(target=sing)


if __name__ == "__main__":
    main()
