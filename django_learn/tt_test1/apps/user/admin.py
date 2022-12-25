from apps.user.models import User
from django.contrib import admin


def upper_case_name(obj):
    return User.USER_DICT[int(obj.is_merchant)]


upper_case_name.short_description = '权限'


class UserModelsAdmin(admin.ModelAdmin):
    list_display = ('username', upper_case_name)


# Register your models here.
admin.site.register(User, UserModelsAdmin)
