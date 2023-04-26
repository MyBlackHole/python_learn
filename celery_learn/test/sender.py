from celery import Celery, chain

app = Celery(
    "project_name",
    broker="redis://localhost:6379",
    backend="redis://localhost:6379",
)

tasks = [
    app.signature(
        f"test.test_app.waiter",
        queue=f"test-worker",
    )
]

chain(*tasks).apply_async(task_id="test")
