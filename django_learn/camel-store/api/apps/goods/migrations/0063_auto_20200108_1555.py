# Generated by Django 2.1.8 on 2020-01-08 07:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('goods', '0062_auto_20191205_1656'),
    ]

    operations = [
        migrations.RenameField(
            model_name='replgoodstype',
            old_name='price',
            new_name='credit',
        ),
        migrations.AlterField(
            model_name='replgoodstype',
            name='credit',
            field=models.PositiveIntegerField(default=0, verbose_name='积分'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='replgoodstype',
            name='market_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='市场价格'),
        ),
        migrations.AddField(
            model_name='replgoodstype',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='价格'),
        ),
    ]