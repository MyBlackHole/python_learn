import redis

r = redis.Redis(decode_responses=True)
r.zadd("test_zset", {"value": 1000})
r.zadd("test_zset", {"tom": 5000})
r.zadd("test_zset", {"joe": 3400})
print(r.zrevrangebyscore("test_zset", float("-inf"), 2000))
print(r.zrevrangebyscore("test_zset", 10000, 2000))


# python3 zset.py
# ['tom', 'joe']
