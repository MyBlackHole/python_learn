from apps.goods.models import *
from apps.order.models import OrderGoods
# http://127.0.0.1:8000
from apps.user.models import User
from django.core.cache import cache
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from django_redis import get_redis_connection


# Create your views here.


class IndexView(View):
    """首页"""

    def get(self, request):
        """显示首页"""
        context = cache.get('index_page_data')

        if context is None:
            print('设置缓存')
            types = GoodsType.objects.all()

            goods_banners = IndexGoodsBanner.objects.all()

            promotion_banners = IndexPromotionBanner.objects.all()

            goods_sku_all = GoodsSKU.objects.all().order_by('-create_time')

            # print(goods_sku_all)
            context = {'types': types,
                       'goods_banners': goods_banners,
                       'promotion_banners': promotion_banners,
                       'goods_sku_all': goods_sku_all}
            cache.set('index_page_data', context, 3600)

        user = request.user
        cart_count = 0
        if user.is_authenticated:
            conn = get_redis_connection('default')
            cart_key = 'cart_%d' % user.id
            cart_count = conn.hlen(cart_key)
        context.update(cart_count=cart_count)
        return render(request, 'index.html', context)


# /shop/商家id
class ShopView(View):
    """商家首页"""

    def get(self, request, shop_id):
        try:
            name = User.objects.get(id=shop_id)
        except User.DoesNotExist:
            return redirect(reverse('goods:index'))

        shop_sku_list = GoodsSKU.objects.filter(merchant_id=shop_id)

        activity_list = IndexPromotionBanner.objects.filter(merchant_id=shop_id)

        shop_spu_list = Goods.objects.filter(merchant_id=shop_id)

        wheel_list = IndexGoodsBanner.objects.filter(merchant_id=shop_id)[:3]

        print(shop_spu_list)

        context = {'name': name,
                   'shop_spu_list': shop_spu_list,
                   'shop_sku_list': shop_sku_list,
                   'wheel_list': wheel_list,
                   'activity_list': activity_list}
        return render(request, 'shop.html', context)


# /goods/商品id
class DetailView(View):
    """详情页"""

    def get(self, request, goods_id):
        """显示详情页"""
        try:
            sku = GoodsSKU.objects.get(id=goods_id)
        except GoodsSKU.DoesNotExist:
            return redirect(reverse('goods:index'))

        types = GoodsType.objects.all()

        sku_orders = OrderGoods.objects.filter(sku=sku).exclude(comment='')

        new_skus = GoodsSKU.objects.filter(merchant_id=sku.merchant_id).order_by('-create_time')[:2]

        sku_goos_type = Goods.objects.get(id=sku.goods_id)

        same_spu_skus = GoodsSKU.objects.filter(goods=sku.goods).exclude(id=goods_id)

        user = request.user
        cart_count = 0
        if user.is_authenticated:
            conn = get_redis_connection('default')
            cart_key = 'cart_%d' % user.id
            cart_count = conn.hlen(cart_key)

            conn = get_redis_connection('default')
            history_key = 'history_%d' % user.id
            conn.lrem(history_key, 0, goods_id)
            conn.lpush(history_key, goods_id)
            conn.ltrim(history_key, 0, 4)

        context = {'sku': sku, 'sku_goos_type': sku_goos_type,
                   'sku_orders': sku_orders,
                   'new_skus': new_skus,
                   'same_spu_skus': same_spu_skus,
                   'cart_count': cart_count}

        return render(request, 'detail.html', context)


class ListView(View):
    """type列表页"""

    def get(self, request, type_id, page):
        """显示列表页"""
        # 获取种类信息
        try:
            type = GoodsType.objects.get(id=type_id)
        except GoodsType.DoesNotExist:
            return redirect(reverse('goods:index'))

        types = GoodsType.objects.all()

        sort = request.GET.get('sort')

        goods_ids = Goods.objects.filter(type_id=type_id)

        skus_list = []

        if sort == 'price':
            for goods_id in goods_ids:
                skus = GoodsSKU.objects.filter(goods_id=goods_id).order_by('price')
                skus_list += skus
        elif sort == 'hot':
            for goods_id in goods_ids:
                skus = GoodsSKU.objects.filter(goods_id=goods_id).order_by('-sales')
                skus_list += skus
        else:
            sort = 'default'
            for goods_id in goods_ids:
                skus = GoodsSKU.objects.filter(goods_id=goods_id).order_by('-id')
                skus_list += skus

        print(goods_ids)

        paginator = Paginator(skus_list, 4)

        try:
            page = int(page)
        except Exception as e:
            page = 1

        if page > paginator.num_pages:
            page = 1

        skus_page = paginator.page(page)

        # todo: 进行页码的控制，页面上最多显示5个页码
        num_pages = paginator.num_pages
        if num_pages < 5:
            pages = range(1, num_pages + 1)
        elif page <= 3:
            pages = range(1, 6)
        elif num_pages - page <= 2:
            pages = range(num_pages - 4, num_pages + 1)
        else:
            pages = range(page - 2, page + 3)
        goods_sku_all = []
        for goods_id in goods_ids:
            goods_sku = GoodsSKU.objects.filter(goods_id=goods_id).order_by('-create_time')[:2]
            goods_sku_all += goods_sku

        user = request.user
        cart_count = 0
        if user.is_authenticated:
            conn = get_redis_connection('default')
            cart_key = 'cart_%d' % user.id
            cart_count = conn.hlen(cart_key)

        context = {'goods_ids': goods_ids,
                   'type': type,
                   'types': types,
                   'skus_page': skus_page,
                   'goods_sku_all': goods_sku_all,
                   'cart_count': cart_count,
                   'pages': pages,
                   'sort': sort}

        return render(request, 'list.html', context)


class SpuListView(View):
    """Goods列表页"""

    def get(self, request, goods_id, page):
        """显示列表页"""
        # 获取种类信息
        try:
            goods_id = Goods.objects.get(id=goods_id)
            type = GoodsType.objects.get(id=goods_id.type_id)
        except GoodsType.DoesNotExist:
            return redirect(reverse('goods:index'))

        sort = request.GET.get('sort')

        if sort == 'price':
            skus = GoodsSKU.objects.filter(goods_id=goods_id).order_by('price')
        elif sort == 'hot':
            skus = GoodsSKU.objects.filter(goods_id=goods_id).order_by('-sales')
        else:
            sort = 'default'
            skus = GoodsSKU.objects.filter(goods_id=goods_id).order_by('-id')

        paginator = Paginator(skus, 4)

        try:
            page = int(page)
        except Exception as e:
            page = 1

        if page > paginator.num_pages:
            page = 1

        skus_page = paginator.page(page)

        # todo: 进行页码的控制，页面上最多显示5个页码
        num_pages = paginator.num_pages
        if num_pages < 5:
            pages = range(1, num_pages + 1)
        elif page <= 3:
            pages = range(1, 6)
        elif num_pages - page <= 2:
            pages = range(num_pages - 4, num_pages + 1)
        else:
            pages = range(page - 2, page + 3)

        goods_sku_all = GoodsSKU.objects.filter(goods_id=goods_id).order_by('-create_time')[:2]

        context = {'skus_page': skus_page,
                   'pages': pages,
                   'goods': goods_id,
                   'type': type,
                   'goods_sku_all': goods_sku_all,
                   'sort': sort}

        return render(request, 'spu_list.html', context)
