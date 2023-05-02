import sys

import kombu
from kombu import pidbox


def callback():
    print("callback")


def main(arguments):
    connection = kombu.Connection("redis://localhost:6379")
    mailbox = pidbox.Mailbox("testMailbox", type="direct")
    bound = mailbox(connection)
    bound._broadcast("print_msg", {"msg": "Message for you"})


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
