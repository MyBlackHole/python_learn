# 模型
from django.db import models


# 添加模型
class UserInfo(models.Model):
    USER_TYPE = (
        (1, '普通用户'),
        (2, 'VIP'),
        (3, 'SVIP'),
    )

    # IntegerField:int  枚举
    user_type = models.IntegerField(choices=USER_TYPE)
    # CharField:字符
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)


class UserToken(models.Model):
    # OneToOneField:一对一
    user = models.OneToOneField(UserInfo, on_delete=models.CASCADE)
    token = models.CharField(max_length=64)
