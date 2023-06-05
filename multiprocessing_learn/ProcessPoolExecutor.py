import time
from concurrent.futures import ProcessPoolExecutor


def task(sleep_sec=10, tag="test"):
    print("[%s] start sleep" % tag)
    time.sleep(sleep_sec)
    print("%s" % sleep_sec)
    print("[%s] finish sleep" % tag)
    return sleep_sec


def main():
    # process_pool = ProcessPoolExecutor(max_workers=3)
    # future = process_pool.submit(task, 3, tag="TEST")
    # ret = future.result()
    # print("result is %s" % str(ret))
    # process_pool.shutdown()

    with ProcessPoolExecutor(max_workers=3) as pool:
        pool_result = list(pool.map(task, range(10), chunksize=4))
    if pool_result:
        for result in pool_result:
            print(result)


if __name__ == "__main__":
    main()
