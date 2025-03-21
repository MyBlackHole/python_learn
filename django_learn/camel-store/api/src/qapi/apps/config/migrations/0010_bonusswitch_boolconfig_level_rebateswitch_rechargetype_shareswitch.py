# Generated by Django 2.1.2 on 2018-11-21 08:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('config', '0009_notice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True, verbose_name='会员等级名称')),
                ('threshold', models.DecimalField(decimal_places=2, max_digits=15, unique=True, verbose_name='充值金额门槛')),
                ('discount', models.PositiveSmallIntegerField(default=0, verbose_name='折扣')),
            ],
            options={
                'verbose_name': '会员等级',
                'verbose_name_plural': '会员等级',
                'ordering': ('threshold',),
            },
        ),
        migrations.CreateModel(
            name='RechargeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15, unique=True, verbose_name='充值金额')),
                ('real_pay', models.DecimalField(decimal_places=2, max_digits=15, unique=True, verbose_name='实付金额')),
            ],
            options={
                'verbose_name': '优惠充值',
                'verbose_name_plural': '优惠充值',
                'ordering': ('amount',),
            },
        ),
        migrations.CreateModel(
            name='BoolConfig',
            fields=[
            ],
            options={
                'verbose_name': '开关式配置项',
                'verbose_name_plural': '开关式配置项',
                'proxy': True,
                'indexes': [],
            },
            bases=('config.systemconfig',),
        ),
        migrations.CreateModel(
            name='BonusSwitch',
            fields=[
            ],
            options={
                'verbose_name': '分销返利设置',
                'verbose_name_plural': '分销返利设置',
                'proxy': True,
                'indexes': [],
            },
            bases=('config.boolconfig',),
        ),
        migrations.CreateModel(
            name='RebateSwitch',
            fields=[
            ],
            options={
                'verbose_name': '推广返利设置',
                'verbose_name_plural': '推广返利设置',
                'proxy': True,
                'indexes': [],
            },
            bases=('config.boolconfig',),
        ),
        migrations.CreateModel(
            name='ShareSwitch',
            fields=[
            ],
            options={
                'verbose_name': '显示分享设置',
                'verbose_name_plural': '显示分享设置',
                'proxy': True,
                'indexes': [],
            },
            bases=('config.boolconfig',),
        ),
    ]
