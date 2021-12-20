import pika
import json

credentials = pika.PlainCredentials('black', '1358')  # mq用户名和密码
# 虚拟队列需要指定参数 virtual_host，如果是默认的可以不填。
connection = pika.BlockingConnection(pika.ConnectionParameters(host = '192.168.5.233',port = 5672,virtual_host = '/',credentials = credentials))
channel=connection.channel()
# 声明exchange，由exchange指定消息在哪个队列传递，如不存在，则创建。durable = True 代表exchange持久化存储，False 非持久化存储
channel.exchange_declare(exchange = 'python-test',durable = True, exchange_type='direct')

for i in range(10):
    message=json.dumps({'OrderId':"1000%s"%i})
# 指定 routing_key。delivery_mode = 2 声明消息在队列中持久化，delivery_mod = 1 消息非持久化
    channel.basic_publish(exchange = 'python-test',routing_key = 'OrderId',body = message,
                          properties=pika.BasicProperties(delivery_mode = 2))
    print(message)
connection.close()
