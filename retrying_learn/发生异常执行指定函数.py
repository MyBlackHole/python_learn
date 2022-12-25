import requests
from retrying import RetryError, retry


def retry_if_io_error(exception):
    """Return True if we should retry (in this case when it's an IOError), False otherwise"""
    print("ok")
    print(str(exception))
    return isinstance(exception, AssertionError)


@retry(retry_on_exception=retry_if_io_error, stop_max_attempt_number=5)
def might_io_error():
    print("Retry forever with no wait if an IOError occurs, raise any other errors")
    i = 1 / 0
    assert 1 > 2, "异常"


class A:
    count = 7

    @retry(wrap_exception=True, stop_max_attempt_number=count)
    def only_raise_retry_error_when_not_io_error(self):
        print(
            "Retry forever with no wait if an IOError occurs, raise any other errors wrapped in RetryError"
        )
        # requests.get(url='sdjf')
        # i = 1 / 0
        assert 1 > 2, "异常信息"

    # only_raise_retry_error_when_not_io_error()


def retry_if_result_none(result):
    """Return True if we should retry (in this case when result is None), False otherwise"""
    print(result)
    return result is None


@retry(
    wrap_exception=True, retry_on_result=retry_if_result_none, stop_max_attempt_number=5
)
def might_io_error1():
    print("Retry forever with no wait if an IOError occurs, raise any other errors")
    assert 1 > 2, "lll"
    # return 1


a = A()
try:
    # p = a.only_raise_retry_error_when_not_io_error()
    might_io_error1()
    # i = 1 / 0
except Exception as e:
    # except RetryError as e:
    print(e.args[0].value)
