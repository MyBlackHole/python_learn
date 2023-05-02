import sys

import kombu
from kombu import pidbox

hostname = "localhost"
connection = kombu.Connection("redis://localhost:6379")
mailbox = pidbox.Mailbox("testMailbox", type="direct")
node = mailbox.Node(hostname, state={"a": "b"})
node.channel = connection.channel()


def callback(body, message):
    print(body)
    print(message)


def main(arguments):
    consumer = node.listen(callback=callback)
    try:
        while True:
            print("Consumer Waiting")
            connection.drain_events()
    finally:
        consumer.cancel()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
