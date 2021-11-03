from django.db import models


# Create your models here.


class GoodsCategory(models.Model):
    """商品分类"""
    CATEGORY_TYPE = (
        (1, "一级类目"),
        (2, "二级类目"),
        (3, "三级类目"),
    )

    name = models.CharField("类别", default="", max_length=30, help_text="类别名")
    code = models.CharField("类别code", default="", max_length=30, help_text="类别名code")
    desc = models.TextField("类别描述", default="", help_text="类别描述")
