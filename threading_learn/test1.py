from threading import Thread
import time

aa = list(range(10))

class DemandUser(object):
    demand_user = None
    run_status = 1

    def __new__(cls, *args, **kwargs):
        if not cls.demand_user:
            cls.demand_user = super(DemandUser, cls).__new__(cls, *args, **kwargs)
        return cls.demand_user

    def __init__(self):
        self.GET_CRAWLER_COMMENT_USER_URL = 'http://119.3.208.208:8010/Comment/SelectBlogger'
        self.crawler_demand_user = []
        if self.run_status:
            self.run_status = 0
            Thread(target=self.timing_update_user).start()
    
    def timing_update_user(self):
        time.sleep(30)


def task1(times):
    global aa
    while True:
        aa = list(range(times))
        dem = DemandUser()
        print(id(dem))


def task2(times):
    while True:
        aaa = aa.copy()
        print(aaa)


def run():
    t1 = Thread(target=task1, args=[10])
    # t1 = Thread(target=task1, args=[3]).start()
    # t1 = Thread(target=task1, args=[8]).start()
    # t2 = Thread(target=task2, args=[5]).start()
    # # 给t1开启守护线程
    # t1.setDaemon(True)
    t1.start()
    # t2.start()
    print('__main__')
    # 注释这行将不会输出task1
    t1.join()



if __name__ == "__main__":
    run()
