# Generated by Django 2.1 on 2019-05-21 23:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('goods', '0002_auto_20190522_0708'),
        ('order', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='orderinfo',
            name='addr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Address', verbose_name='地址'),
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='merchant',
            field=models.ForeignKey(limit_choices_to={'is_merchant': True}, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='merchant_id', to=settings.AUTH_USER_MODEL, verbose_name='商家用户'),
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_id',
                                    to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='ordergoods',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.OrderInfo',
                                    verbose_name='订单'),
        ),
        migrations.AddField(
            model_name='ordergoods',
            name='sku',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsSKU',
                                    verbose_name='商品SKU'),
        ),
    ]