from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import SaleUser
from .forms import UserChangeForm, UserCreationForm





admin.site.site_header = 'Sale R&D Panel Admin'
admin.site.site_title = 'R&D'
admin.site.index_title = 'R&D Panel'





class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ["email", 'name', 'username', 'user_role',]
    list_filter = ["name", "username"]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Permissions", {"fields": ["is_active", "is_admin", "is_superuser"]}),
    ]

    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "username", "password1", "password2", "is_active", "is_admin", "is_superuser"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []


admin.site.register(SaleUser, UserAdmin)
admin.site.unregister(Group)