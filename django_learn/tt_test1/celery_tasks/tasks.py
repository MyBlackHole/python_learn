# 使用celery
import os
import time

import django
from django.conf import settings
from django.core.mail import send_mail
from django.template import loader

# 在任务处理者一端加这几句
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tt_test1.settings")
django.setup()

from celery import Celery
from apps.goods.models import GoodsType, IndexGoodsBanner, IndexPromotionBanner, GoodsSKU

# 创建一个独立存储路径Celery类的实例对象
app = Celery('celery_tasks.tasks', broker='redis://1260.0.1:6379/6')


# 定义任务函数
# 独立app存储路径代理
@app.task
# @shared_task
def send_register_active_email(to_email, username, token):
    """发送激活邮件"""
    subject = '期待您的加入'
    message = ''
    sender = settings.EMAIL_FROM
    receiver = [to_email]
    html_message = '<h1>%s, 欢迎您注册会员</h1>请点击下面链接激活您的账户<br/><a href="http://192.168.42.50/user/active/%s">http://192.168.42.50/user/active/%s</a>' % (
        username, token, token)

    send_mail(subject, message, sender, receiver, html_message=html_message)
    time.sleep(5)


@app.task
def generate_static_index_html():
    """产生首页静态页面"""
    types = GoodsType.objects.all()

    goods_banners = IndexGoodsBanner.objects.all()

    promotion_banners = IndexPromotionBanner.objects.all()

    goods_sku_all = GoodsSKU.objects.all()

    context = {'types': types,
               'goods_banners': goods_banners,
               'promotion_banners': promotion_banners,
               'goods_sku_all': goods_sku_all}

    temp = loader.get_template('index.html')
    static_index_html = temp.render(context)

    save_path = os.path.join(settings.BASE_DIR, 'static/index.html')
    with open(save_path, 'w') as f:
        f.write(static_index_html)
