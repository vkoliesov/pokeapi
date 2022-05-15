from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from accounts.models import User


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['username','email', 'first_name', 'last_name']
    fieldsets = (
        (None, {'fields': ('username','email', 'password')}),
        (_('Personal Info'), {'fields': ('first_name','last_name','phone_number')}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','email', 'password1', 'password2')
            }),
    )


admin.site.register(User, UserAdmin)
