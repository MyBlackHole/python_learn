# Generated by Django 2.1.2 on 2018-10-22 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('goods', '0015_auto_20181019_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodtype',
            name='asset_ratio',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='返利比例(:%)'),
        ),
        migrations.AlterField(
            model_name='goodtype',
            name='goods',
            field=models.ForeignKey(help_text='商品', on_delete=django.db.models.deletion.CASCADE, related_name='gtypes',
                                    to='goods.Goods', verbose_name='商品'),
        ),
    ]