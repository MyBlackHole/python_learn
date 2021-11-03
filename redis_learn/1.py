import redis

GROUPNAME = 'tf::'
# REDIS_HOST = '127.0.0.1'
REDIS_HOST = 'localhost'
REDIS_POST = 6379
REDIS_DB = 8

# 创建连接池
redis_pool = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_POST, db=REDIS_DB)

# 创建连接(并使用连接池)
def new_redis_conn(redis_pool):
    redis_conn = redis.Redis(connection_pool=redis_pool)
    return redis_conn

redis_conn = new_redis_conn(redis_pool)
# resp = redis_conn.ttl('djfjj')
# print(resp)
# print(type(resp))

# data = redis_conn.rpop('a')
# print(data)
print('ok')
# 查询key = 'a', 没有返回None
# data = redis_conn.get('a')
# print(data)

# data = redis_conn.ttl('a')
# print(data)

# data = redis_conn.mget('c')
# print(data)
# for i in data:
#     if not i:
#         print(i)
#
# # 成功返回True
# status = redis_conn.set('a', 123, ex=-1)
# print(status)

# status = redis_conn.zadd('a', {'celery-taskset-meta-7d2ccaa4-fac6-4a6c-a3a7-a5696db57dd0': 1629198396})
# print(status)

r = redis_conn.zrevrangebyscore("text1", 1629498396, 0)
print(r)

r = redis_conn.type("text11")
print(r)

print(redis_conn.exists("ok"))

# r = redis_conn.rename("text1", "text")
# print(r)


# print('status', status)
#
# _dict = {"1": "2", "2": "3"}
# print(redis_conn.mset(_dict))
# print(_dict.items())
