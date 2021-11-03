from booktest.models import GoodsInfo
from django.contrib import admin


# Register your models here.
class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['id']


admin.site.register(GoodsInfo, GoodsInfoAdmin)
