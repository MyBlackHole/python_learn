from kombu import Connection

with Connection("amqp://guest:guest@172.17.0.2:5672//") as conn:
    simple_queue = conn.SimpleQueue("simple_queue")
    message = simple_queue.get(block=True, timeout=1)
    print(f"Received: {message.payload}")
    message.ack()
    simple_queue.close()
