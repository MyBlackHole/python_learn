# Generated by Django 2.1.7 on 2019-03-05 07:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('account', '0020_auto_20190301_1152'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wxuseraccount',
            options={'permissions': (('change_account', '赠送扣减用户账户金额和积分'),), 'verbose_name': '用户账户',
                     'verbose_name_plural': '用户账户'},
        ),
        migrations.AddField(
            model_name='wxusercreditlog',
            name='number',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='订单编号或拼团编号'),
        ),
    ]