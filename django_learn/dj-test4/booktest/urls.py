"""test4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from booktest import views
from django.urls import re_path

app_name = 'booktest'
urlpatterns = [

    re_path(r'^index$', views.index, name='index'),
    re_path(r'^index2$', views.index2),  # 模板 文件加载顺序

    re_path(r'^temp_var$', views.temp_var),  # 模板变量
    re_path(r'^temp_tags$', views.temp_tags),  # 模板标签
    re_path(r'^temp_filter$', views.temp_filter),  # 模板过滤器

    re_path(r'^temp_inherit$', views.temp_inherit),  # 模板继承
    #
    re_path(r'^html_escape$', views.html_escape),  # html转义

    re_path(r'^login$', views.login),  # 显示登录页面
    re_path(r'^login_check$', views.login_check),  # 进行登录校验
    re_path(r'^change_pwd$', views.change_pwd),  # 修改密码页面显示
    re_path(r'^change_pwd_action$', views.change_pwd_action),  # 修改密码处理

    re_path(r'^verify_code$', views.verify_code),  # 产生验证码图片

    re_path(r'^re_path_reverse$', views.url_reverse),  # re_path反向解析页面
    re_path(r'^show_args/(\d+)/(\d+)$', views.show_args, name='show_args'),  # 捕获位置参数
    re_path(r'^show_kwargs/(?P<c>\d+)/(?P<b>\d+)$', views.show_kwargs, name='show_kwargs'),  # 捕获关键字参数

    re_path(r'^test_redirect$', views.test_redirect),
]
