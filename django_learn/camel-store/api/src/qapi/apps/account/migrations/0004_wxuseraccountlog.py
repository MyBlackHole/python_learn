# Generated by Django 2.0.7 on 2018-07-23 09:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('wxapp', '0002_wxuser_qrcode_url'),
        ('account', '0003_auto_20180717_2258'),
    ]

    operations = [
        migrations.CreateModel(
            name='WxUserAccountLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_type',
                 models.CharField(choices=[('asset', '分销'), ('use', '抵现'), ('use_return', '取消订单返还')], max_length=32,
                                  verbose_name='类型')),
                ('asset', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='金额')),
                ('remark', models.CharField(blank=True, default='', max_length=2048, verbose_name='备注')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='增加时间')),
                ('referral', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                               related_name='referral_account_logs', to='wxapp.WxUser',
                                               verbose_name='帮手')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_logs',
                                           to='wxapp.WxUser', verbose_name='用户')),
            ],
            options={
                'verbose_name': '佣金记录',
                'verbose_name_plural': '佣金记录',
                'ordering': ('-add_time',),
            },
        ),
    ]