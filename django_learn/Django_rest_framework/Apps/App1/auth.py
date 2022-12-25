# 认证
from rest_framework.authentication import BaseAuthentication
from Apps.App1 import models
from rest_framework import exceptions


class Authentication(BaseAuthentication):  # 分离出来
    """认证"""

    def authenticate(self, request):
        token = request._request.GET.get('token')
        print("进来了")
        # first() 查询首个无则返回None
        token_obj = models.UserToken.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed('用户认证失败')
        # 在rest framework内部会将这两个字段赋值给request，以供后续操作使用
        return (token_obj.user, token_obj)

    def authenticate_header(self, request):
        pass
