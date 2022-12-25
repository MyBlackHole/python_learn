from apps.order.views import *
from django.urls import re_path

app_name = 'order'
urlpatterns = [
    re_path(r'^place$', OrderPlaceView.as_view(), name='place'),  # 提交订单页面显示
    re_path(r'^commit$', OrderCommitView.as_view(), name='commit'),  # 订单创建
    re_path(r'^pay$', OrderPayView.as_view(), name='pay'),  # 订单支付
    re_path(r'^paysku$', OrderPaySKUView.as_view(), name='paysku'),  # 订单商品处理
    re_path(r'^skufahuo$', FaHuoView.as_view(), name='skufahuo'),  # 商品发货
    re_path(r'^check$', CheckPayView.as_view(), name='check'),  # 查询支付交易结果
    re_path(r'^comment/(?P<order_id>.+)/(?P<sku_id>\d+)$', CommentView.as_view(), name='comment'),  # 订单评论
]
