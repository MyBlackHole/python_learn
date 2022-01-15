import multiprocessing

multiprocessing.set_start_method('spawn', force=True)


def func():
    print("ok")


if __name__ == "__main__":
    multiprocessing.Process(target=func).start()
