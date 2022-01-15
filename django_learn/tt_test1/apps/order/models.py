from db.base_model import BaseModel
from django.db import models


# Create your models here.


class OrderInfo(BaseModel):
    """订单模型类"""
    PAY_METHODS = {
        '1': "货到付款",
        '2': "微信支付",
        '3': "支付宝",
        '4': '银联支付'
    }

    PAY_METHOD_CHOICES = (
        (1, '货到付款'),
        (2, '微信支付'),
        (3, '支付宝'),
        (4, '银联支付')
    )

    PAY_STATUS = (
        (1, '未支付'),
        (2, '已支付')
    )

    PAY_STATUS_DICT = {
        1: '未支付',
        2: '已支付'
    }
    order_id = models.CharField(max_length=128, primary_key=True, verbose_name='订单id')
    user = models.ForeignKey('user.User', verbose_name='用户', on_delete=models.CASCADE, related_name='user_id')
    addr = models.ForeignKey('user.Address', verbose_name='地址', on_delete=models.CASCADE)
    pay_method = models.SmallIntegerField(choices=PAY_METHOD_CHOICES, default=3, verbose_name='支付方式')
    total_count = models.IntegerField(default=1, verbose_name='商品数量')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='商品总价')
    transit_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='订单运费')
    pay_status = models.SmallIntegerField(choices=PAY_STATUS, default=1, verbose_name='支付状态')
    trade_no = models.CharField(max_length=128, verbose_name='支付编号')

    def __str__(self):
        return self.order_id

    class Meta:
        db_table = 'df_order_info'
        verbose_name = '订单'
        verbose_name_plural = verbose_name


class OrderGoods(BaseModel):
    ORDER_STATUS_CHOICES = (
        (1, '待支付'),
        (2, '待发货'),
        (3, '待收货'),
        (4, '待评价'),
        (5, '已完成')
    )

    ORDER_STATUS = {
        1: '待支付',
        2: '待发货',
        3: '待收货',
        4: '待评价',
        5: '已完成'
    }

    """订单商品模型类"""
    order = models.ForeignKey('OrderInfo', verbose_name='订单', on_delete=models.CASCADE)
    merchant = models.ForeignKey('user.User', verbose_name='商家', on_delete=models.CASCADE,
                                 limit_choices_to={'is_merchant': True})
    order_status = models.SmallIntegerField(choices=ORDER_STATUS_CHOICES, default=1, verbose_name='订单状态')
    sku = models.ForeignKey('goods.GoodsSKU', verbose_name='商品SKU', on_delete=models.CASCADE)
    count = models.IntegerField(default=1, verbose_name='商品数目')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='商品价格')
    comment = models.CharField(max_length=256, default='', verbose_name='评论')

    def __str__(self):
        return self.order.order_id

    class Meta:
        db_table = 'df_order_goods'
        verbose_name = '订单商品'
        verbose_name_plural = verbose_name
