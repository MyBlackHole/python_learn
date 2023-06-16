from datetime import datetime

import pytz
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler(
    next_run_time=datetime.now,
)

scheduler.configure(timezone=pytz.timezone("Asia/Shanghai"))


def test():
    print("hello", datetime.now())


# job = scheduler.add_job(test, "interval", seconds=30, id="my_job_id")
scheduler.add_job(
    test,
    "interval",
    seconds=30,
    id="my_job_id",
    next_run_time=datetime.now(),
    # next_run_time=None,
)

# print(datetime.now())
scheduler.start()
