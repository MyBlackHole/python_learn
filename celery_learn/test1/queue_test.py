if __name__ == "__main__":
    from celery import Celery
    app = Celery(
        broker="redis://localhost:6379",
        # broker=conf.get("celery", "broker_url"),
    )
    queues_dict = app.control.inspect().active_queues()
    print(queues_dict)
