# Generated by Django 2.1.2 on 2018-11-02 09:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('account', '0011_wxuseraccountlog_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='withdraw',
            name='status',
            field=models.IntegerField(choices=[(0, '提现中'), (2, '提现失败'), (1, '提现完成')], default=0, verbose_name='提现状态'),
        ),
    ]
