from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import BlockedIP
from .forms import UserAdminCreationForm, UserAdminChangeForm

admin.site.register(BlockedIP)
User = get_user_model()


class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = [
        "username",
        "first_name",
        "last_name",
        "is_active",
        "is_superuser",
    ]
    list_filter = ("is_active", "is_superuser")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "username",
                    "password",
                )
            },
        ),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "last_name",
                    "first_name",
                    "username",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    search_fields = ("email", "username", "first_name", "last_name",)
    ordering = ("email", "first_name", "last_name")
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
