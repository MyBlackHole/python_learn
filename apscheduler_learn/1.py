from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler


def test_clock():
    print(f"{datetime.now()}")


if __name__ == "__main__":
    schelers = BlockingScheduler()
    schelers.a_job(test_clock, "interval", secons=3)

    schelers.start()
