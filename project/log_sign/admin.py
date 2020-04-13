from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import normal_user
# Register your models here.


class normal_user_inline(admin.TabularInline):
    model = normal_user
    can_delete = False
    verbose_name_plural = 'normal_user'


class UserAdmin(BaseUserAdmin):
    inlines = (normal_user_inline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
