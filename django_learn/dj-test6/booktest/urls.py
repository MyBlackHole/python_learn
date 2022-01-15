from booktest import views
from django.urls import re_path

urlpatterns = [
    re_path(r'^$', views.index),
    re_path(r'^editor/', views.editor),
    re_path(r'^show/', views.show),
    re_path(r'^query/', views.query),
    re_path(r'^send/$', views.send),
    re_path(r'^sathello$', views.sayhello),
    re_path(r'^set_session$', views.set_session),
    re_path(r'^get_session$', views.get_session),
]
