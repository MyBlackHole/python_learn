# Generated by Django 2.1.5 on 2019-01-30 04:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('goods', '0041_auto_20190129_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='attach',
            field=models.ManyToManyField(blank=True, related_name='attach_goods', to='goods.Attach',
                                         verbose_name='自定义信息'),
        ),
    ]