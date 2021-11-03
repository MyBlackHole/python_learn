from datetime import datetime

from django.contrib.auth.models import AbstractUser  # 抽象用户
from django.db import models


# Create your models here.

class UserProfile(AbstractUser):
    """用户信息"""
    GENDER_CHOICES = (
        ("male", u"男"),
        ("female", u"女")
    )
    # 手机注册，允许姓名、生日、邮箱为空
    name = models.CharField("姓名", max_length=30, null=True, blank=True)
    birthday = models.DateField("出生年月", null=True, blank=True)
    gender = models.CharField("性别", max_length=6, choices=GENDER_CHOICES, default="female")
    mobile = models.CharField("电话", max_length=11)
    email = models.CharField("邮箱", max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class VerifyCode(models.Model):
    """验证码"""
    code = models.CharField("验证码", max_length=10)
    mobile = models.CharField("电话", max_length=11)
    add_time = models.DateField("添加时间", default=datetime.now)

    class Meta:
        verbose_name = "短信验证"
        verbose_name_plural = verbose_name
