import time

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


# app = Celery('tasks', broker='redis://127.0.0.1:6379/0')

@shared_task
def sayhello():
    print('hello……')
    time.sleep(6)
    print('world……')
    return 'OK'


@shared_task
def sendopen():
    print('开始发送邮件！！！')
    msg = '<a href="http://127.0.0.1:8000" target="_blank">点击激活</a>'
    send_mail('注册激活', '', settings.EMAIL_FROM,
              ['15077459464@163.com'],
              html_message=msg)
    print("发送成功！！")
    return "OK"
