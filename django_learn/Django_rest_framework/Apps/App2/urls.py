from django.urls import path, re_path
from .views import UserView, ParserView, RolesView, Create, UserInfoView, GroupView, UserGroupView, Pager1View

urlpatterns = [
    # 获取版本
    # path('users/', UserView.as_view()), # /api2/users/?version=v2
    re_path('(?P<version>[v1|v2]+)/users/', UserView.as_view(), name='api_user'),  # /api2/v2/users/ 必须使用re_path支持re

    re_path('initialize/', Create.as_view()),  # 初始化对象

    path('parser/', ParserView.as_view(), ),  # 解析

    # 序列化
    re_path('(?P<version>[v1|v2]+)/roles/', RolesView.as_view()),  # 序列化
    re_path('(?P<version>[v1|v2]+)/info/', UserInfoView.as_view()),  # 序列化
    re_path('(?P<version>[v1|v2]+)/group/(?P<pk>\d+)/', GroupView.as_view(), name='gp'),  # 序列化生成url

    # 序列化验证
    re_path('(?P<version>[v1|v2]+)/usergroup/', UserGroupView.as_view(), ),  # 序列化做验证

    # 分页
    re_path('(?P<version>[v1|v2]+)/pager1/', Pager1View.as_view(), )  # 分页1
]
