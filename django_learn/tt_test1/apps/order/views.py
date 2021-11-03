from datetime import datetime

from apps.goods.models import *
from apps.order.models import *
from apps.user.models import *
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django_redis import get_redis_connection
from utils.mixin import LoginRequiredMixin


# /order/place
class OrderPlaceView(LoginRequiredMixin, View):
    """提交订单页面显示"""

    def post(self, request):
        """提交订单页面显示"""
        user = request.user
        sku_ids = request.POST.getlist('sku_ids')  # [1,26]

        if not sku_ids:
            return redirect(reverse('cart:show'))

        conn = get_redis_connection('default')
        cart_key = 'cart_%d' % user.id

        skus = []
        total_count = 0
        total_price = 0
        for sku_id in sku_ids:
            sku = GoodsSKU.objects.get(id=sku_id)
            count = conn.hget(cart_key, sku_id)
            amount = sku.price * int(count)
            sku.count = count
            sku.amount = amount
            skus.append(sku)
            total_count += int(count)
            total_price += amount

        transit_price = 10

        total_pay = total_price + transit_price

        addrs = Address.objects.filter(user=user)

        sku_ids = ','.join(sku_ids)
        context = {'skus': skus,
                   'total_count': total_count,
                   'total_price': total_price,
                   'transit_price': transit_price,
                   'total_pay': total_pay,
                   'addrs': addrs,
                   'sku_ids': sku_ids}

        return render(request, 'place_order.html', context)


class OrderCommitView1(View):
    """订单创建"""

    @transaction.atomic
    def post(self, request):
        '''订单创建'''
        user = request.user
        if not user.is_authenticated():
            return JsonResponse({'res': 0, 'errmsg': '用户未登录'})

        addr_id = request.POST.get('addr_id')
        pay_method = request.POST.get('pay_method')
        sku_ids = request.POST.get('sku_ids')  # 1,3

        if not all([addr_id, pay_method, sku_ids]):
            return JsonResponse({'res': 1, 'errmsg': '参数不完整'})

        if pay_method not in OrderInfo.PAY_METHODS.keys():
            return JsonResponse({'res': 2, 'errmsg': '非法的支付方式'})

        try:
            addr = Address.objects.get(id=addr_id)
        except Address.DoesNotExist:
            return JsonResponse({'res': 3, 'errmsg': '地址非法'})

        # todo: 创建订单核心业务

        order_id = datetime.now().strftime('%Y%m%d%H%M%S') + str(user.id)

        transit_price = 10

        total_count = 0
        total_price = 0

        save_id = transaction.savepoint()
        try:
            # todo: 向df_order_info表中添加一条记录
            order = OrderInfo.objects.create(order_id=order_id,
                                             user=user,
                                             addr=addr,
                                             pay_method=pay_method,
                                             total_count=total_count,
                                             total_price=total_price,
                                             transit_price=transit_price)

            # todo: 用户的订单中有几个商品，需要向df_order_goods表中加入几条记录
            conn = get_redis_connection('default')
            cart_key = 'cart_%d' % user.id

            sku_ids = sku_ids.split(',')
            for sku_id in sku_ids:
                try:
                    sku = GoodsSKU.objects.select_for_update().get(id=sku_id)
                except:
                    transaction.savepoint_rollback(save_id)
                    return JsonResponse({'res': 4, 'errmsg': '商品不存在'})

                print('user:%d stock:%d' % (user.id, sku.stock))
                import time
                time.sleep(10)

                count = conn.hget(cart_key, sku_id)

                # todo: 判断商品的库存
                if int(count) > sku.stock:
                    transaction.savepoint_rollback(save_id)
                    return JsonResponse({'res': 6, 'errmsg': '商品库存不足'})

                # todo: 向df_order_goods表中添加一条记录
                OrderGoods.objects.create(order=order,
                                          sku=sku,
                                          count=count,
                                          merchant=sku.merchant,
                                          price=sku.price)

                # todo: 更新商品的库存和销量
                sku.stock -= int(count)
                sku.sales += int(count)
                sku.save()

                # todo: 累加计算订单商品的总数量和总价格
                amount = sku.price * int(count)
                total_count += int(count)
                total_price += amount

            # todo: 更新订单信息表中的商品的总数量和总价格
            order.total_count = total_count
            order.total_price = total_price
            order.save()
        except Exception as e:
            transaction.savepoint_rollback(save_id)
            return JsonResponse({'res': 7, 'errmsg': '下单失败'})

        transaction.savepoint_commit(save_id)

        # todo: 清除用户购物车中对应的记录
        conn.hdel(cart_key, *sku_ids)

        return JsonResponse({'res': 5, 'message': '创建成功'})


class OrderCommitView(View):
    """订单创建"""

    @transaction.atomic
    def post(self, request):
        '''订单创建'''
        user = request.user
        if not user.is_authenticated:
            return JsonResponse({'res': 0, 'errmsg': '用户未登录'})

        addr_id = request.POST.get('addr_id')
        pay_method = request.POST.get('pay_method')
        sku_ids = request.POST.get('sku_ids')  # 1,3

        if not all([addr_id, pay_method, sku_ids]):
            return JsonResponse({'res': 1, 'errmsg': '参数不完整'})

        if pay_method not in OrderInfo.PAY_METHODS.keys():
            return JsonResponse({'res': 2, 'errmsg': '非法的支付方式'})

        try:
            addr = Address.objects.get(id=addr_id)
        except Address.DoesNotExist:
            return JsonResponse({'res': 3, 'errmsg': '地址非法'})

        # todo: 创建订单核心业务

        order_id = datetime.now().strftime('%Y%m%d%H%M%S') + str(user.id)

        transit_price = 10

        total_count = 0
        total_price = 0

        save_id = transaction.savepoint()
        try:
            # todo: 向df_order_info表中添加一条记录
            order = OrderInfo.objects.create(order_id=order_id,
                                             user=user,
                                             addr=addr,
                                             pay_method=pay_method,
                                             total_count=total_count,
                                             total_price=total_price,
                                             transit_price=transit_price)

            # todo: 用户的订单中有几个商品，需要向df_order_goods表中加入几条记录
            conn = get_redis_connection('default')
            cart_key = 'cart_%d' % user.id

            sku_ids = sku_ids.split(',')
            for sku_id in sku_ids:
                for i in range(3):
                    try:
                        sku = GoodsSKU.objects.get(id=sku_id)
                    except:
                        transaction.savepoint_rollback(save_id)
                        return JsonResponse({'res': 4, 'errmsg': '商品不存在'})

                    count = conn.hget(cart_key, sku_id)

                    # todo: 判断商品的库存
                    if int(count) > sku.stock:
                        transaction.savepoint_rollback(save_id)
                        return JsonResponse({'res': 6, 'errmsg': '商品库存不足'})

                    # todo: 更新商品的库存和销量
                    orgin_stock = sku.stock
                    new_stock = orgin_stock - int(count)
                    new_sales = sku.sales + int(count)

                    res = GoodsSKU.objects.filter(id=sku_id, stock=orgin_stock).update(stock=new_stock, sales=new_sales)
                    if res == 0:
                        if i == 2:
                            transaction.savepoint_rollback(save_id)
                            return JsonResponse({'res': 7, 'errmsg': '下单失败2'})
                        continue

                    # todo: 向df_order_goods表中添加一条记录
                    OrderGoods.objects.create(order=order,
                                              sku=sku,
                                              merchant=sku.merchant,
                                              count=count,
                                              price=sku.price)

                    # todo: 累加计算订单商品的总数量和总价格
                    amount = sku.price * int(count)
                    total_count += int(count)
                    total_price += amount

                    break

            # todo: 更新订单信息表中的商品的总数量和总价格
            order.total_count = total_count
            order.total_price = total_price
            order.save()
        except Exception as e:
            transaction.savepoint_rollback(save_id)
            return JsonResponse({'res': 7, 'errmsg': '下单失败'})

        transaction.savepoint_commit(save_id)

        # todo: 清除用户购物车中对应的记录
        conn.hdel(cart_key, *sku_ids)

        return JsonResponse({'res': 5, 'message': '下单成功'})


# /order/pay
class OrderPayView(View):
    """用户订单处理"""

    def post(self, request):
        '''订单处理'''
        user = request.user
        if not user.is_authenticated:
            return JsonResponse({'res': 0, 'errmsg': '用户未登录'})

        order_id = request.POST.get('order_id')

        if not order_id:
            return JsonResponse({'res': 1, 'errmsg': '无效的订单id'})

        try:
            order = OrderInfo.objects.get(order_id=order_id)
        except OrderInfo.DoesNotExist:
            return JsonResponse({'res': 2, 'errmsg': '订单错误'})
        if order.trade_no == 1:
            return JsonResponse({'res': 3, 'errmsg': "你已经支付过了！！！"})
        if order.pay_status == 1:
            order.pay_status = 2
            order.trade_no = 1
            order.save()
            order_skus = OrderGoods.objects.filter(order=order.order_id)
            for order_sku in order_skus:
                order_sku.order_status = 2
                order_sku.save()
            return JsonResponse({'res': 4, 'message': "支付完成"})
        else:
            return JsonResponse({'res': 6, 'errmsg': "你不具备此操作"})


# /order/paysku
class OrderPaySKUView(View):
    """用户订单处理"""

    def post(self, request):
        """订单处理"""
        user = request.user
        if not user.is_authenticated:
            return JsonResponse({'res': 0, 'errmsg': '用户未登录'})

        order_sku_id = request.POST.get('order_sku_id')
        order_id = request.POST.get('order_id')

        if not order_sku_id:
            return JsonResponse({'res': 1, 'errmsg': '无效的订单id'})

        try:
            order_sku = OrderGoods.objects.get(sku_id=order_sku_id, order_id=order_id)
        except OrderInfo.DoesNotExist:
            return JsonResponse({'res': 2, 'errmsg': '订单错误'})
        if order_sku.order_status == 1:
            return JsonResponse({'res': 3, 'errmsg': '您还未支付'})
        elif order_sku.order_status == 3:
            order_sku.order_status = 4
            order_sku.save()
            return JsonResponse({'res': 4, 'message': "收货成功"})


# /order/skufahuo
class FaHuoView(View):
    """用户订单处理"""

    def post(self, request):
        """订单处理"""
        user = request.user
        if not user.is_authenticated:
            return JsonResponse({'res': 0, 'errmsg': '用户未登录'})

        order_sku_id = request.POST.get('order_sku_id')

        if not order_sku_id:
            return JsonResponse({'res': 1, 'errmsg': '无效的订单id'})

        try:
            order_sku = OrderGoods.objects.get(id=order_sku_id)
        except OrderInfo.DoesNotExist:
            return JsonResponse({'res': 2, 'errmsg': '订单错误'})
        if order_sku.order_status == 2:
            order_sku.order_status = 3
            order_sku.save()
            return JsonResponse({'res': 4, 'message': "发货成功"})


# /order/check
class CheckPayView(View):
    """查看订单支付的结果"""

    def post(self, request):
        """查询支付结果"""
        user = request.user
        if not user.is_authenticated:
            return JsonResponse({'res': 0, 'errmsg': '用户未登录'})

        order_id = request.POST.get('order_id')

        if not order_id:
            return JsonResponse({'res': 1, 'errmsg': '无效的订单id'})

        try:
            order = OrderInfo.objects.get(order_id=order_id,
                                          user=user,
                                          pay_method=1,
                                          trade_no=1,
                                          order_status=1)
        except OrderInfo.DoesNotExist:
            return JsonResponse({'res': 2, 'errmsg': '订单错误'})

        return JsonResponse({'res': 3, 'message': '支付成功'})


class CommentView(LoginRequiredMixin, View):
    """订单评论"""

    def get(self, request, order_id, sku_id):
        """提供评论页面"""
        user = request.user

        if not order_id:
            return redirect(reverse('user:order', args=(1,)))

        try:
            order = OrderInfo.objects.get(order_id=order_id, user=user)
        except OrderInfo.DoesNotExist:
            return redirect(reverse('user:order', args=(1,)))

        order.status_name = OrderInfo.PAY_STATUS_DICT[order.pay_status]
        print(order_id, sku_id)
        try:
            order_sku = OrderGoods.objects.get(order_id=order_id, sku_id=sku_id)
        except OrderGoods.DoesNotExist:
            return redirect(reverse('user:order', args=(1,)))
        amount = order_sku.count * order_sku.price
        order_sku.amount = amount
        order.order_sku = order_sku

        return render(request, "order_comment.html", {"order": order})

    def post(self, request, order_id, sku_id):
        """处理评论内容"""
        user = request.user
        if not order_id:
            return redirect(reverse('user:order', args=(1,)))

        try:
            order = OrderInfo.objects.get(order_id=order_id, user=user)
        except OrderInfo.DoesNotExist:
            return redirect(reverse('user:order', args=(1,)))

        content = request.POST.get('content')
        try:
            order_goods = OrderGoods.objects.get(order=order, sku_id=sku_id)
        except OrderGoods.DoesNotExist:
            return redirect(reverse('user:order', args=(1,)))

        order_goods.comment = content
        order_goods.order_status = 5
        order_goods.save()
        return redirect(reverse("user:order", kwargs={"page": 1}))
