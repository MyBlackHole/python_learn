import json

from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, HttpResponse
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.versioning import QueryParameterVersioning
from rest_framework import serializers
from .pager import PagerSerialiser

# 忽略全部认证与权限
from Apps.App2 import models


class ALL_authenticate():
    authentication_classes = []
    permission_classes = []
    throttle_classes = []


class UserView(APIView):
    authentication_classes = []
    permission_classes = []
    throttle_classes = []

    # versioning_class = QueryParameterVersioning  # version=xxx

    def get(self, request, *args, **kwargs):
        print('get version')
        # 获取版本
        print(request.version)
        print(request.versioning_scheme)
        # 获取浏览器访问的url，reverse反向解析
        # 需要两个参数：viewname就是url中的别名，request=request是url中要传入的参数
        # (?P<version>[v1|v2]+)/users/，这里本来需要传version的参数，但是version包含在request里面（源码里面可以看到），所有只需要request=request就可以
        url_path = request.versioning_scheme.reverse(viewname='api_user', request=request)
        print(url_path)
        return HttpResponse(request.version)


class Create(ALL_authenticate, APIView):

    def get(self, request, *args, **kwargs):
        models.Role.objects.update_or_create(title='校长')
        models.Role.objects.update_or_create(title='老师')
        models.Role.objects.update_or_create(title='学生')
        return HttpResponse('role initialize success!!')


class ParserView(ALL_authenticate, APIView):
    # JSONParser：表示只能解析content-type:application/json的头
    # FormParser:表示只能解析content-type:application/x-www-form-urlencoded的头
    # MultipartParser:表示只能解析multipart/form-data的头

    # parser_classes = [JSONParser, FormParser, MultiPartParser]

    def post(self, request, *args, **kwargs):
        print(request.data)
        return HttpResponse(request.data)


# 要先写一个序列化的类
class RolesSerializer(serializers.Serializer):
    # Role表里面的字段id和title序列化
    id = serializers.IntegerField()
    title = serializers.CharField()


class RolesView(ALL_authenticate, APIView):

    def get(self, request, *args, **kwargs):
        # # 方式一：对于[obj,obj,obj]
        # # （Queryset）
        # roles = models.Role.objects.all()
        # # 序列化，两个参数，instance:接受Queryset（或者对象）   mangy=True表示对Queryset进行处理，mant=False表示对对象进行进行处理
        # ser = RolesSerializer(instance=roles, many=True)
        # # 转成json格式，ensure_ascii=False表示显示中文，默认为True
        # ret = json.dumps(ser.data, ensure_ascii=False)

        # 方式二：
        role = models.Role.objects.all().first()  # 返回第一个
        ser = RolesSerializer(instance=role, many=False)
        ret = json.dumps(ser.data, ensure_ascii=False)
        return HttpResponse(ret)


# 方式一
# class UserInfoSerializer(serializers.Serializer):
#     """序列化用户的信息"""
#     # user_type是choices（1,2,3），显示全称的方法用source
#     type = serializers.CharField(source="get_user_type_display")
#     username = serializers.CharField()
#     password = serializers.CharField()
#     # group.title：组的名字
#     group = serializers.CharField(source="group.title")
#     # SerializerMethodField(),表示自定义显示
#     # 然后写一个自定义的方法
#     rls = serializers.SerializerMethodField()
#
#     def get_rls(self, row):
#         # 获取用户所有的角色
#         role_obj_list = row.roles.all()
#         ret = []
#         # 获取角色的id和名字
#         # 以字典的键值对方式显示
#         for item in role_obj_list:
#             ret.append({"id": item.id, "title": item.title})
#         return ret

# 方式二
class UserInfoSerializer(serializers.ModelSerializer):
    """序列化用户的信息"""

    # type = serializers.CharField(source="get_user_type_display")
    # group = serializers.CharField(source="group.title")
    # rls = serializers.SerializerMethodField()
    #
    # def get_rls(self, row):
    #     # 获取用户所有的角色
    #     role_obj_list = row.roles.all()
    #     ret = []
    #     # 获取角色的id和名字
    #     # 以字典的键值对方式显示
    #     for item in role_obj_list:
    #         ret.append({"id": item.id, "title": item.title})
    #     return ret
    #
    # class Meta:
    #     model = models.UserInfo
    #     fields = ['id', 'username', 'password', 'type', 'group', 'rls']

    # 反序列化成url
    group = serializers.HyperlinkedIdentityField(view_name='gp', lookup_field='group_id', lookup_url_kwarg='pk')

    # 方式三
    class Meta:
        model = models.UserInfo
        # fields = "__all__"
        fields = ['id', 'username', 'password', 'group', 'roles']
        # 表示连表的深度
        depth = 1


class UserInfoView(ALL_authenticate, APIView):
    """用户的信息"""

    def get(self, request, *args, **kwargs):
        users = models.UserInfo.objects.all()
        # ser = UserInfoSerializer(instance=users, many=True)

        # 序列化url
        # 这里必须要传参数context={'request':request}
        ser = UserInfoSerializer(instance=users, many=True, context={'request': request})
        ret = json.dumps(ser.data, ensure_ascii=False)
        return HttpResponse(ret)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserGroup
        fields = "__all__"


class GroupView(ALL_authenticate, APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        obj = models.UserGroup.objects.filter(pk=pk).first()

        ser = GroupSerializer(instance=obj, many=False)
        ret = json.dumps(ser.data, ensure_ascii=False)
        return HttpResponse(ret)


# 自定义验证规则
class GroupValidation(object):
    def __init__(self, base):
        self.base = base

    def __call__(self, value):
        if not value.startswith(self.base):
            message = "标题必须以%s为开头" % self.base
            raise serializers.ValidationError(message)


class UserGroupSerializer(serializers.Serializer):
    # title = serializers.CharField()
    # 使用自定义验证
    title = serializers.CharField(validators=[GroupValidation('a'), ])


class UserGroupView(ALL_authenticate, APIView):
    def post(self, request, *args, **kwargs):
        ser = UserGroupSerializer(data=request.data)
        # 数据验证
        if ser.is_valid():
            print(ser.validated_data['title'])
        else:
            print(ser.errors)

        return HttpResponse("用户提交数据验证")


# 自定义分页类
class MyPageNumberPagination(PageNumberPagination):
    # 每页显示多少个
    page_size = 3
    # 默认每页显示3个，可以通过传入pager1/?page=2&size=4,改变默认每页显示的个数
    page_size_query_param = "size"
    # 最大页数不超过10
    max_page_size = 10
    # 获取页码数的
    page_query_param = "page"


# 自定义分页2
class MyLimitOffsetPagination(LimitOffsetPagination):
    # 默认显示的个数
    default_limit = 2
    # 当前的位置
    offset_query_param = "offset"
    # 通过limit改变默认显示的个数
    limit_query_param = "limit"
    # 一页最多显示的个数
    max_limit = 10


# 自定义分页类3 (加密分页)
class MyCursorPagination(CursorPagination):
    # 加密分页
    cursor_query_param = "cursor"
    page_size = 2  # 每页显示2个数据
    ordering = 'id'  # 排序
    page_size_query_param = None
    max_page_size = None


# 分页
class Pager1View(ALL_authenticate, APIView):
    def get(self, request, *args, **kwargs):
        # 获取所有数据
        roles = models.Role.objects.all()
        # 创建分页对象，这里是自定义的MyPageNumberPagination
        pg = MyCursorPagination()
        # 获取分页的数据
        page_roles = pg.paginate_queryset(queryset=roles, request=request, view=self)
        # 对数据进行序列化
        ser = PagerSerialiser(instance=page_roles, many=True)
        # return Response(ser.data)
        # 同时返回上下页连接
        return pg.get_paginated_response(ser.data)
