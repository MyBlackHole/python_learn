# Generated by Django 2.0.7 on 2018-07-27 09:13

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('goods', '0008_auto_20180727_1203'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goods',
            old_name='num',
            new_name='asset_ratio_1',
        ),
        migrations.RenameField(
            model_name='goods',
            old_name='num2',
            new_name='asset_ratio_2',
        ),
    ]