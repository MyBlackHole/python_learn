from redis import Redis

uri = "redis://:redisp!3Sw0rd@192.168.125.177:6379/3"

redis_client = Redis.from_url(uri, health_check_interval=10, decode_responses=True)
print(redis_client.ping())
for value in redis_client.keys("*"):
    print(value)
