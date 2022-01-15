from booktest import views
from django.urls import re_path

urlpatterns = [
    re_path('^index$', views.index),
    re_path('^login$', views.login),
    re_path('^login_check$', views.login_check),
    re_path('^test_ajax$', views.ajax_test),
    re_path('^ajax_handle$', views.ajax_handle),
    re_path('^login_ajax$', views.login_ajax),
    re_path('^login_ajax_check$', views.login_ajax_check),
    re_path(r'^set_cookie$', views.set_cookie),  # 设置cookie
    re_path(r'^get_cookie$', views.get_cookie),  # 获取cookie

    re_path(r'^set_session$', views.set_session),  # 设置session
    re_path(r'^get_session$', views.get_session),  # 获取session
    re_path(r'^clear_session$', views.clear_session),  # 清除session
]
