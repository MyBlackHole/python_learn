# Generated by Django 2.1.4 on 2019-01-16 03:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('goods', '0037_migrate_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='groupbuy',
            field=models.BooleanField(default=False, verbose_name='是否拼团'),
        ),
    ]