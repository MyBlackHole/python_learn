import consul
import json

c = consul.Consul(host="192.168.5.229", port=8500)

# poll a key for updates
index = None
while True:
    print(1)
    time = 60 * 60 * 24
    index, data = c.kv.get('config_52', index=index, wait=f"{time}s")
    print(json.loads(data['Value']))
    # break

# in another process
# c.kv.put('foo', '金斯克决定了算法计算的理解的房间里所'.encode())
