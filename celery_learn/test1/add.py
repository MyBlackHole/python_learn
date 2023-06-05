from task import waiter

if __name__ == "__main__":
    async_result = waiter.delay(23610)
    print(async_result)
