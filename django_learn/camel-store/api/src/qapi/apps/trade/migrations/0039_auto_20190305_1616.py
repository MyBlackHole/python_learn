# Generated by Django 2.1.7 on 2019-03-05 08:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('trade', '0038_orders_fictitious'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsbackup',
            name='g_rebate',
            field=models.PositiveIntegerField(null=True, verbose_name='返利金额'),
        ),
    ]
