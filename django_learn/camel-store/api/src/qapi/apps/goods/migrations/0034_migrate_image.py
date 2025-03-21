# Generated by Django 2.1.4 on 2019-01-04 08:56

from django.db import migrations
from django.db import transaction


def migrate_goods_image(apps, schema_editor):
    # 迁移商品的轮播图和详情图片到Images表
    # from apps.goods.models import Goods, Images
    Goods = apps.get_model("goods", "Goods")
    Images = apps.get_model("goods", "Images")
    GoodsImage = apps.get_model("goods", "GoodsImage")
    DetailImage = apps.get_model("goods", "DetailImage")
    with transaction.atomic():
        for goods in Goods.objects.all():
            for banner in GoodsImage.objects.filter(goods=goods):
                instance = Images.objects.create(image=banner.image, index=banner.index)
                goods.banner.add(instance)
            for detail in DetailImage.objects.filter(goods=goods):
                instance = Images.objects.create(image=detail.image, index=detail.index)
                goods.detail.add(instance)


class Migration(migrations.Migration):
    dependencies = [
        ('goods', '0033_auto_20190104_1656'),
    ]

    operations = [

        migrations.RunPython(migrate_goods_image),

        # 删除多余图片表
        migrations.RemoveField(
            model_name='detailimage',
            name='goods',
        ),
        migrations.RemoveField(
            model_name='detailimage',
            name='image',
        ),
        migrations.RemoveField(
            model_name='goodsimage',
            name='goods',
        ),
        migrations.RemoveField(
            model_name='goodsimage',
            name='image',
        ),
        migrations.DeleteModel(
            name='DetailImage',
        ),
        migrations.DeleteModel(
            name='GoodsImage',
        ),
    ]
