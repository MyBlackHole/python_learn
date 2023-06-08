import os
import signal
import threading
from time import sleep


Global_MAX = 100
Global_Count = 0


class AIOBashOperator:
    def execute(self, context):
        print(os.getpid())
        event = threading.Event()

        monitor = threading.Thread(
            target=AIOBaseOperator.monitoring_store,
            args=(event, context),
        )
        monitor.start()

        while True:
            sleep(1)
            global Global_Count
            Global_Count += 1
            print("execute Global_Count", Global_Count)
            if Global_Count > 40:
                break
        event.set()


class AIOBaseOperator:
    @staticmethod
    def monitoring_store(event, context):
        print(os.getpid())
        while not event.is_set():
            sleep(5)
            if Global_Count > 20:
                os.kill(os.getpid(), signal.SIGTERM)
                # os._exit(1)
            print("monitoring Global_Count", Global_Count)


def handle_signal(signum, frame):
    print("signum", signum, "frame", frame)
    raise Exception("退出")


if __name__ == "__main__":
    signal.signal(signal.SIGTERM, handle_signal)
    AIOBashOperator().execute(None)
