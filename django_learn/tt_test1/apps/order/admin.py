from django.contrib import admin

from .models import OrderGoods


# Register your models here.
class OrderModelsAdmin(admin.ModelAdmin):
    exclude = ['is_delete']
    list_display = ('order', 'sku', 'count')
    # list_display_links = None


admin.site.register(OrderGoods, OrderModelsAdmin)
