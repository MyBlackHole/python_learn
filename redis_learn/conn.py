import redis

# 单连接
# r = redis.Redis(host='127.0.0.1', port=6379)

# 连接池
pool = redis.ConnectionPool(host='127.0.0.1', port=6379)

r = redis.StrictRedis(connection_pool=pool)
print(r.get('1').decode())
