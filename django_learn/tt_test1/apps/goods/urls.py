from apps.goods.views import IndexView, DetailView, ListView, ShopView, SpuListView
from django.urls import re_path

app_name = 'goods'
urlpatterns = [
    re_path(r'^$', IndexView.as_view(), name='index'),  # 首页
    re_path(r'^shop/(?P<shop_id>\d+)$', ShopView.as_view(), name='shop'),  # 商家首页
    re_path(r'^goods/(?P<goods_id>\d+)$', DetailView.as_view(), name='detail'),  # 详情页
    re_path(r'^list/(?P<type_id>\d+)/(?P<page>\d+)$', ListView.as_view(), name='list'),  # 列表页
    re_path(r'^spulist/(?P<goods_id>\d+)/(?P<page>\d+)$', SpuListView.as_view(), name='spulist'),  # 列表页
]
