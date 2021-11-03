from django.urls import re_path

from apps.cart.views import *

app_name = 'cart'
urlpatterns = [
    re_path(r'^add$', CartAddView.as_view(), name='add'),
    re_path(r'^$', CartInfoView.as_view(), name='show'),
]
