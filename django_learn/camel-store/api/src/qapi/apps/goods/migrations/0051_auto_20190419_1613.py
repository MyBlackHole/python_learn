# Generated by Django 2.1.7 on 2019-04-19 08:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('qfile', '0004_auto_20190222_1822'),
        ('goods', '0050_auto_20190416_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodtype',
            name='icon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    to='qfile.File', verbose_name='图标'),
        ),
        migrations.AddField(
            model_name='replgoodstype',
            name='icon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    to='qfile.File', verbose_name='图标'),
        ),
        migrations.AddField(
            model_name='subgoodstype',
            name='icon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    to='qfile.File', verbose_name='图标'),
        ),
    ]