# Generated by Django 2.1.7 on 2019-05-07 02:14

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('goods', '0057_remove_goodscategory_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='postage',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name='运费'),
        ),
    ]