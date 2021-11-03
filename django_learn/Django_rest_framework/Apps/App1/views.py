from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from django.views import View
from Apps.App1 import models
from Apps.App1.auth import Authentication
from Apps.App1.permission import MyPremission
from Apps.App1.throttle import VisitThrottle

ORDER_DICT = {
    1: {
        'name': 'apple',
        'price': 15
    },
    2: {
        'name': 'dog',
        'price': 100
    }
}


def md5(user):
    import hashlib
    import time
    # 当前时间，相当于生成一个随机的字符串
    ctime = str(time.time())
    m = hashlib.md5(bytes(user, encoding='utf-8'))
    m.update(bytes(ctime, encoding='utf-8'))
    return m.hexdigest()


# 添加用户名密码
class Create(APIView):
    def get(self, request, *args, **kwargs):
        # 创建用户
        # update_or_create:存在则更新不存在创建
        models.UserInfo.objects.update_or_create(user_type=1, username='black', password='123456')
        return JsonResponse({'status': '创建成功'})


class AuthView(APIView):
    # 为空代表不认证
    authentication_classes = []

    # 为空代表不需要权限
    permission_classes = []

    # # 默认的节流是登录用户（10/m）,AuthView不需要登录，这里用匿名用户的节流（3/m）
    throttle_classes = [VisitThrottle, ]

    def post(self, request, *args, **kwargs):
        ret = {'code': 1000, 'msg': None}
        try:
            # 提取输出username
            user = request._request.POST.get('username')  # _request APIView
            # 提取输出password
            pwd = request._request.POST.get('password')
            print(user, pwd)
            obj = models.UserInfo.objects.filter(username=user, password=pwd).first()
            if not obj:
                ret['code'] = 1001
                ret['msg'] = '用户名或密码错误'
            # 为用户创建token
            token = md5(user)
            # 存在就更新，不存在就创建
            models.UserToken.objects.update_or_create(user=obj, defaults={'token': token})
            ret['token'] = token
        except Exception as e:
            ret['code'] = 1002
            ret['msg'] = '请求异常'

        # 机器
        xff = request.META.get('HTTP_X_FORWARDED_FOR')

        # ip
        remote_addr = request.META.get('REMOTE_ADDR')
        print(xff, remote_addr)
        return JsonResponse(ret)


class OrderView(APIView):
    """订单相关业务"""

    authentication_classes = [Authentication, ]  # 添加认证
    permission_classes = []

    def get(self, request, *args, **kwargs):
        # self.dispatch
        # 认证必然返回参数
        print(request.user.username)
        print(request.auth.token)

        ret = {'code': 1000, 'msg': None, 'data': None}
        try:
            ret['data'] = ORDER_DICT
        except Exception as e:
            pass
        return JsonResponse(ret)


class UserInfoView(APIView):
    """ 订单相关业务(普通用户和VIP用户可以看)"""
    permission_classes = [MyPremission, ]  # 不用全局的权限配置的话，这里就要写自己的局部权限

    def get(self, request, *args, **kwargs):
        print(request.user)
        return HttpResponse(request.user.username)
