import time
import functools
from concurrent import futures

executor = futures.ThreadPoolExecutor(1)


def timeout(seconds):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            future = executor.submit(func, *args, **kw)
            return future.result(timeout=seconds)

        return wrapper

    return decorator


@timeout(2)
def task(a, b):
    time.sleep(1.2)
    return a + b


task(2, 3)
