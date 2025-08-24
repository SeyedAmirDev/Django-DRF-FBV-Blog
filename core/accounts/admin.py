from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("email", "is_staff", "is_superuser", "is_active")
    search_fields = ("email", )
    list_filter = ("is_staff", "is_superuser", "is_active")
    ordering = ("email",)

    fieldsets = (
        (_('Authentication'), {"fields": ("email", "password")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
        (
            _('Group Permissions'),
            {
                "fields": (
                    "groups",
                    "user_permissions",
                )
            }
        ),
        (_("Important dates"), {"fields": ("last_login", "created_date", "updated_date")}),
    )
    readonly_fields = ("last_login", "created_date", "updated_date")

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "is_staff", "is_active", "is_superuser",
                           "password1", "password2"),
            },
        ),
    )