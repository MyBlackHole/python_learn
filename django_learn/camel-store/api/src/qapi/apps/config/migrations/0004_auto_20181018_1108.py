# Generated by Django 2.1.2 on 2018-10-18 03:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('config', '0003_faqcontent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faqcontent',
            name='icon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    to='qfile.File', verbose_name='图标'),
        ),
    ]