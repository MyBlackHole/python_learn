from flask import Flask
import datetime
from flask_apscheduler import APScheduler

aps = APScheduler()


class Config(object):
    JOBS = [
        {
            "id": "job1",
            "func": "scheduler:task",
            "args": (1, 2),
            "trigger": "cron",
            "day": "*",
            "hour": "*",
            "minute": "*",
            "second": "20",
        }
    ]
    SCHEDULER_API_ENABLED = True


def task(a, b):
    print(
        str(datetime.datetime.now()) + " execute task " + "{}+{}={}".format(a, b, a + b)
    )


if __name__ == "__main__":
    app = Flask(__name__)
    app.config.from_object(Config())

    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()

    app.run(port=8000)
