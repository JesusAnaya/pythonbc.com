from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe
from .models import User


class CustomUserAdmin(UserAdmin):
    list_per_page = 20

    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        (('Personal info'), {
            'fields': ('first_name', 'last_name', 'email')
        }),
        (('Profile'), {
            'fields': ('photo', 'biography', 'google_plus')
        }),
        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions')
        }),
        (('Important dates'), {
            'fields': ('last_login', 'date_joined')
        }),
    )

    list_display = (
        'image', 'username', 'email', 'first_name', 'last_name',
        'is_staff', 'is_superuser'
    )

    def image(self, obj):
        tag = "<img src='/media/{0}' height='60'>"
        return mark_safe(tag.format(obj.photo))


admin.site.register(User, CustomUserAdmin)
