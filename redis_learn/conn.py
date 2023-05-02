import redis

# 单连接
# r = redis.Redis(host='127.0.0.1', port=6379)

# 连接池
pool = redis.ConnectionPool(host="127.0.0.1", port=6379, db=2)

r = redis.StrictRedis(connection_pool=pool)
r.rpush("list", "test")
r.rpush("list", "test1")
print(r.rpop("list").decode())
