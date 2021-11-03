import time
from celery import Celery
from celery import uuid
from config import BROKER_URL, CELERY_RESULT_BACKEND

#实例化Celery对象
app = Celery(
    'celeryDemo',
    broker=BROKER_URL,
    backend=CELERY_RESULT_BACKEND
)

# 添加@app.task()装饰器，说明执行的任务是一个异步任务
@app.task()
def add(x,y):
    print('task enter ....')
    print(x)
    print(y)
    time.sleep(5)
    return x+y


@app.task()
def add1(x,y):
    print('add1 uuid')
    print(x)
    print(y)
    time.sleep(5)
    return x+y

@app.task()
def add2(x,y):
    print('add1 uuid')
    print(x)
    print(y)
    time.sleep(5)
    return x+y
