import re

from apps.goods.models import *
from apps.order.models import *
from apps.user.models import *
from celery_tasks.tasks import send_register_active_email
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from django_redis import get_redis_connection
from itsdangerous import SignatureExpired
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from utils.mixin import LoginRequiredMixin


# Create your views here.

# /user/register
class RegisterView(View):
    """注册"""

    def get(self, request):
        """显示注册页面"""
        return render(request, 'register.html')

    def post(self, request):
        """进行注册处理"""
        username = request.POST.get('user_name')
        pwd = request.POST.get('pwd')
        cpwd = request.POST.get('cpwd')
        email = request.POST.get('email')

        remember = str(request.POST.get('remember'))

        if not all([username, pwd, email]):
            return render(request, 'register.html', {'errmsg': '数据不完整!!!'})
        if pwd != cpwd:
            return render(request, 'register.html', {'errmsg': '密码两次输入不一致！！!'})

        if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            return render(request, 'register.html', {'errmsg': '邮箱格式不正确!!!'})

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None

        if user:
            return render(request, 'register.html', {'errmsg': '用户名已存在'})

        user = User.objects.create_user(username, email, pwd)
        print(remember)
        if remember == 'on':
            group = Group.objects.get(name='商家用户权限')
            user.groups.add(group)
            user.is_merchant = 1
            user.is_staff = 1
        user.is_active = 0
        user.save()

        serializer = Serializer(settings.SECRET_KEY, 3600)
        info = {'confirm': user.id}
        token = serializer.dumps(info)
        token = token.decode()

        send_register_active_email.delay(email, username, token)

        return redirect(reverse('user:login'))


class ActiveView(View):
    """用户激活"""

    def get(self, request, token):
        """进行用户激活"""
        serializer = Serializer(settings.SECRET_KEY, 3600)
        try:
            info = serializer.loads(token)
            user_id = info['confirm']

            user = User.objects.get(id=user_id)
            user.is_active = 1
            user.save()

            return redirect(reverse('user:login'))
        except SignatureExpired as e:
            return HttpResponse('激活链接已过期')


# /user/login
class LoginView(View):
    """登录"""

    def get(self, request):
        """显示登录页面"""
        if 'username' in request.COOKIES:
            username = request.COOKIES.get('username')
            checked = 'checked'
        else:
            username = ''
            checked = ''

        return render(request, 'login.html', {'username': username, 'checked': checked})

    def post(self, request):
        """登录校验"""
        username = request.POST.get('username')
        password = request.POST.get('pwd')
        user = User.objects.get(username=username)
        if not all([username, password]):
            return render(request, 'login.html', {'errmsg': '数据不完整'})

        if user.is_active:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                next_url = request.GET.get('next', reverse('goods:index'))

                response = redirect(next_url)

                remember = str(request.POST.get('remember'))
                if remember == 'on':
                    response.set_cookie('username', username, max_age=7 * 24 * 3600)
                else:
                    response.delete_cookie('username')

                return response
            else:
                return render(request, 'login.html', {'errmsg': '用户名或密码错误!!!'})
        else:
            return render(request, 'login.html', {'errmsg': '账户未激活'})


# /user/logout
class LogoutView(View):
    """退出登录"""

    def get(self, request):
        """退出登录"""
        logout(request)

        return redirect(reverse('goods:index'))


# /user
class UserInfoView(LoginRequiredMixin, View):
    """用户中心-信息页"""

    def get(self, request):
        """显示"""
        user = request.user
        address = Address.objects.get_default_address(user)

        con = get_redis_connection('default')

        history_key = 'history_%d' % user.id

        sku_ids = con.lrange(history_key, 0, 4)

        goods_li = []
        for id in sku_ids:
            goods = GoodsSKU.objects.get(id=id)
            goods_li.append(goods)

        context = {'page': 'user',
                   'address': address,
                   'hidden': 'hidden',
                   'goods_li': goods_li,
                   'is_user': user.is_merchant}

        return render(request, 'user_user.html', context)


# /user/order
class UserOrderView(LoginRequiredMixin, View):
    """用户中心-订单页"""

    def get(self, request, page):
        """显示"""
        user = request.user
        orders = OrderInfo.objects.filter(user=user).order_by('-create_time')

        for order in orders:
            order_skus = OrderGoods.objects.filter(order_id=order.order_id)

            for order_sku in order_skus:
                amount = order_sku.count * order_sku.price
                order_sku.amount = amount
                order_sku.order_status_name = OrderGoods.ORDER_STATUS[order_sku.order_status]

            order.status_name = OrderInfo.PAY_STATUS_DICT[order.pay_status]
            order.order_skus = order_skus

        paginator = Paginator(orders, 2)

        try:
            page = int(page)
        except Exception as e:
            page = 1

        if page > paginator.num_pages:
            page = 1

        order_page = paginator.page(page)

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

        context = {'order_page': order_page,
                   'pages': pages,
                   'hidden': 'hidden',
                   'is_user': user.is_merchant,
                   'page': 'order'}

        return render(request, 'user_order.html', context)


# /user/merchantoOrder
class MerchantOrderView(LoginRequiredMixin, View):
    """用户中心-下单页"""

    def get(self, request, page):
        """显示"""
        user = request.user
        order_skus = OrderGoods.objects.filter(merchant=user).order_by('-create_time')

        for order_sku in order_skus:
            amount = order_sku.count * order_sku.price
            order_sku.amount = amount
            order_sku.order_status_name = OrderGoods.ORDER_STATUS[order_sku.order_status]

        paginator = Paginator(order_skus, 3)
        #
        try:
            page = int(page)
        except Exception as e:
            page = 1

        if page > paginator.num_pages:
            page = 1

        order_page = paginator.page(page)

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

        context = {'order_page': order_page,
                   'pages': pages,
                   'is_user': user.is_merchant,
                   'hidden': 'hidden',
                   'page': 'order'}

        return render(request, 'user_merchant_order.html', context)


# /user/address
class AddressView(LoginRequiredMixin, View):
    """请求用户中心-地址页"""

    def get(self, request):
        """显示"""
        user = request.user

        address = Address.objects.get_default_address(user)
        if address:
            return render(request, 'user_address.html', {'addr': address.addr,
                                                         'is_user': user.is_merchant,
                                                         'receiver': address.receiver,
                                                         'hidden': 'hidden',
                                                         'phone': address.phone})
        else:
            return render(request, 'user_address.html', {'addr': "",
                                                         'receiver': "",
                                                         'is_user': user.is_merchant,
                                                         'hidden': 'hidden',
                                                         'phone': ""})

    def post(self, request):
        """地址的添加"""
        receiver = request.POST.get('receiver')
        addr = request.POST.get('addr')
        zip_code = request.POST.get('zip_code')
        phone = request.POST.get('phone')

        if not all([receiver, addr, phone]):
            return JsonResponse({'errmsg': '数据不完整'})

        if not re.match(r'^1[3|4|5|7|8][0-9]{9}$', phone):
            return JsonResponse({'errmsg': '手机格式不正确'})
        user = request.user

        address = Address.objects.get_default_address(user)

        if address:
            is_default = False
        else:
            is_default = True

        Address.objects.create(user=user,
                               receiver=receiver,
                               addr=addr,
                               zip_code=zip_code,
                               phone=phone,
                               is_default=is_default)

        return JsonResponse({'errmsg': '添加成功!!'})
