# Generated by Django 2.1 on 2019-05-27 16:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('goods', '0006_auto_20190527_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='image',
            field=models.ImageField(default=1, upload_to='spu', verbose_name='商品图片'),
            preserve_default=False,
        ),
    ]