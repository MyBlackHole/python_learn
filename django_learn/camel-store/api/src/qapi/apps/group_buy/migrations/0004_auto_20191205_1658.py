# Generated by Django 2.1.10 on 2019-12-05 08:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('group_buy', '0003_remove_ptgroup_ptgtype_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupbuyinfo',
            name='version_timestamp',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
        migrations.AddField(
            model_name='ptgroup',
            name='version_timestamp',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
    ]