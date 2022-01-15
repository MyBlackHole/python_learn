def task_1():
    n = 0
    while True:
        # for i in range(1000000):
        #     n += 1
        #     if (n > 100000):
        #         print(n)
        # sys.stdout.write("ok\n")
        print("---1----")
        # time.sleep(0.1)
        yield


def task_2():
    while True:
        # sys.stdout.write("on\n")
        print("---2----")
        # time.sleep(0.1)
        yield


def main():
    t1 = task_1()
    t2 = task_2()
    # 先让t1运行一会，当t1中遇到yield的时候，再返回到24行，然后
    # 执行t2，当它遇到yield的时候，再次切换到t1中
    # 这样t1/t2/t1/t2的交替运行，最终实现了多任务....协程
    while True:
        print('t1')
        next(t1)
        print('t2')
        next(t2)


if __name__ == "__main__":
    main()
