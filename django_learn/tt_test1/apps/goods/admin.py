from apps.goods.models import *
from django.contrib import admin
from django.core.cache import cache


# Register your models here.


class BaseModelAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.merchant = request.user
        """新增或更新表中的数据时调用"""
        super().save_model(request, obj, form, change)

        from celery_tasks.tasks import generate_static_index_html
        generate_static_index_html.delay()

        cache.delete('index_page_data')

    def get_form(self, request, obj=None, change=False, **kwargs):
        self.exclude = ("merchant",)
        form = super(BaseModelAdmin, self).get_form(request, obj, **kwargs)
        return form

    def get_queryset(self, request):
        qs = super(BaseModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(merchant=request.user)

    def delete_model(self, request, obj):
        """删除表中的数据时调用"""
        super().delete_model(request, obj)
        from celery_tasks.tasks import generate_static_index_html
        generate_static_index_html.delay()

        cache.delete('index_page_data')


class GoodsTypeAdmin(BaseModelAdmin):
    pass


class IndexGoodsBannerAdmin(BaseModelAdmin):
    def sku_name(obj):

        return obj.sku.name

    sku_name.short_description = '商品名'

    def sku_desc(obj):

        return obj.sku.desc

    sku_desc.short_description = '简介'
    list_display = (sku_name, sku_desc)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if str(request.user) != "admin":
            if db_field.name == "sku":
                kwargs["queryset"] = GoodsSKU.objects.filter(merchant=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class IndexTypeGoodsBannerAdmin(BaseModelAdmin):
    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     print(db_field.name)
    #     # if db_field.name == "type":
    #     #     kwargs["queryset"] = GoodsType.objects.filter(username=request.user)
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)
    pass


class IndexPromotionBannerAdmin(BaseModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if str(request.user) != "admin":
            if db_field.name == "sku":
                kwargs["queryset"] = GoodsSKU.objects.filter(merchant=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class GoodsSKUAdmin(BaseModelAdmin):
    list_display = ('name', 'stock', 'sales', 'status')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if str(request.user) != "admin":
            if db_field.name == "goods":
                kwargs["queryset"] = Goods.objects.filter(merchant=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(GoodsType, GoodsTypeAdmin)
admin.site.register(IndexGoodsBanner, IndexGoodsBannerAdmin)
admin.site.register(Goods, IndexTypeGoodsBannerAdmin)
admin.site.register(IndexPromotionBanner, IndexPromotionBannerAdmin)
admin.site.register(GoodsSKU, GoodsSKUAdmin)
