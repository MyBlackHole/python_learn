from time import sleep

from celery import Celery

app = Celery(
    "celery_test",
    broker="redis://localhost:6379",
    backend="redis://localhost:6379"
    # # pip install celery==4.4.6 起
    # broker="amqp://guest:guest@localhost:5672//",
    # backend="amqp://guest:guest@localhost:5672//"
)

max_timeout_in_seconds = float("inf")
# max_timeout_in_seconds = 10
app.conf.broker_transport_options = {
    "visibility_timeout": max_timeout_in_seconds,
}


@app.task(acks_late=True)
def waiter(sleep_time):
    queues_dict = app.control.inspect().active_queues()
    print(queues_dict)
    print("start waiter")
    sleep(sleep_time)
    print("end waiter")
    return "task finished"
