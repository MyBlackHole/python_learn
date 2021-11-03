from retrying import retry


@retry(stop_max_attempt_number=5, wait_fixed=1000, stop_max_delay=30000)
def stop_after_10_s():
    print("10 秒后停止尝试")
    assert 1 > 2, '忘了'


try:
    stop_after_10_s()
except AssertionError as e:
    print(e)
