# Generated by Django 2.0.2 on 2018-04-09 02:46

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name': '首页轮播', 'verbose_name_plural': '首页轮播'},
        ),
        migrations.AlterModelOptions(
            name='goods',
            options={'verbose_name': '商品信息', 'verbose_name_plural': '商品信息'},
        ),
        migrations.AlterModelOptions(
            name='goodscategory',
            options={'verbose_name': '商品类别', 'verbose_name_plural': '商品类别'},
        ),
        migrations.AlterModelOptions(
            name='goodsimage',
            options={'verbose_name': '商品轮播', 'verbose_name_plural': '商品轮播'},
        ),
        migrations.AlterModelOptions(
            name='hotsearchwords',
            options={'verbose_name': '热搜排行', 'verbose_name_plural': '热搜排行'},
        ),
        migrations.AlterModelOptions(
            name='indexad',
            options={'verbose_name': '首页广告', 'verbose_name_plural': '首页广告'},
        ),
    ]
