if __name__ == "__main__":
    from celery import Celery
    app = Celery(
        broker="redis://192.168.78.212:6379/1",
        # broker=conf.get("celery", "broker_url"),
    )
    import pdb
    pdb.set_trace()
    queues_dict = app.control.inspect().active_queues()
    print(queues_dict)
    # queues_dict.json
