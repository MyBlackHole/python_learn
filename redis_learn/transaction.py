import redis

r = redis.Redis(host="localhost", port=6379, db=1)

pipeline = r.pipeline()

pipeline.hset(
    "user-purchase",
    "customer",
    "keith",
)
pipeline.hset(
    "user-purchase",
    "amount",
    100,
)
pipeline.incr(
    "customer-keith-purchase-count",
)

results = pipeline.execute()
print(results)

# 查询
# HGETALL user-purchase
