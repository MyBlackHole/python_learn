from kombu.pools import producers
from queues import task_exchange

priority_to_routing_key = {
    "high": "hipri",
    "mid": "midpri",
    "low": "lopri",
}


def send_as_task(connection, fun, priority="mid", *args, **kwargs):
    payload = {"fun": print, "args": args, "kwargs": kwargs}
    routing_key = priority_to_routing_key[priority]

    with producers[connection].acquire(block=True) as producer:
        producer.publish(
            payload,
            serializer="pickle",
            compression="bzip2",
            exchange=task_exchange,
            declare=[task_exchange],
            routing_key=routing_key,
        )


if __name__ == "__main__":
    from kombu import Connection
    from tasks import hello_task

    # connection = Connection("amqp://guest:guest@172.17.0.2:5672//")
    connection = Connection("redis://localhost:6379/8")

    args = {
        "event_id": 302002,
        "level": "warning",
        "component": "airflow",
        "code": 2501,
        "task_num": "20230619004388",
        "type": "tdsql",
        "attribute": {
            "resource_id": 3,
            "resrc_name": "tdsql_test",
            "resrc_ipaddr": "192.168.37.38",
            "backup_unit_id": 5,
            "bak_obj_name": "tdsql_test_set@set_1669008240_1",
            "crontab_id": 2,
            "storage_id": 1,
            "storage_host": "192.168.78.213",
            "task_num": "20230619004388",
            "sub_task_id": None,
            "total_task_id": 4388,
            "queue": None,
            "task_instance_key_str": "tiny_tdsql__backup_check__20230619",
            "snapshot_full_name": "",
            "message": "由于  发起的任务  ，所以本次任务自动取消",
        },
    }

    send_as_task(
        connection,
        fun=hello_task,
        args=args,
        kwargs={},
        priority="mid",
    )
