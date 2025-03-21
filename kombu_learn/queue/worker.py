import logging

from kombu.log import get_logger
from kombu.mixins import ConsumerMixin
from kombu.utils.functional import reprcall
from queues import task_queues

logger = get_logger(__name__)


class Worker(ConsumerMixin):
    def __init__(self, connection):
        self.connection = connection

    def get_consumers(self, Consumer, channel):
        return [
            Consumer(
                queues=task_queues,
                accept=["pickle", "json"],
                callbacks=[self.process_task],
            )
        ]

    def process_task(self, body, message):
        fun = body["fun"]
        args = body["args"]
        kwargs = body["kwargs"]
        logger.info("Got task: %s", reprcall(fun.__name__, args, kwargs))
        try:
            fun(*args, **kwargs)
        except Exception as exc:
            logger.error("task raised exception: %r", exc)
        message.ack()


if __name__ == "__main__":
    from kombu import Connection
    from kombu.utils.debug import setup_logging

    # setup root logger
    setup_logging(loglevel=logging.INFO, loggers=[""])

    # with Connection("amqp://guest:guest@172.17.0.2:5672//") as conn:
    # with Connection("redis://localhost:6379") as conn:
    with Connection(
        "redis://localhost:6379/8",
        transport_options={"visibility_timeout": 10},
    ) as conn:
        try:
            worker = Worker(conn)
            worker.run()
        except KeyboardInterrupt:
            print("bye bye")
