import functools
import time

import requests
import trip


def timeit(fn):
    start_time = time.time()
    fn()
    return time.time() - start_time


url = 'http://httpbin.org/get'
times = 10  # 100 changed for inland network delay


def fetch():
    r = [requests.get(url) for i in range(times)]
    return r


@trip.coroutine
def async_fetch():
    r = yield [trip.get(url) for i in range(times)]
    raise trip.Return(r)


print('Non-trip cost: %ss' % timeit(fetch))
print('Trip cost: %ss' % timeit(functools.partial(trip.run, async_fetch)))
