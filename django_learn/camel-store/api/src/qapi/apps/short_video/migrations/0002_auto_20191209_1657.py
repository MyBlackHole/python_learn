# Generated by Django 2.1.10 on 2019-12-09 08:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('short_video', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blockwxuser',
            name='version_timestamp',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
        migrations.AddField(
            model_name='shortvideo',
            name='version_timestamp',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
    ]
