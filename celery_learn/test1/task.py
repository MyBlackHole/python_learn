from time import sleep

from celery import Celery

app = Celery(
    "celery_test", broker="redis://localhost:6379", backend="redis://localhost:6379"
)

max_timeout_in_seconds = 30
app.conf.broker_transport_options = {"visibility_timeout": max_timeout_in_seconds}


@app.task(acks_late=True)
def waiter(sleep_time):
    sleep(sleep_time)
    return "task finished"
