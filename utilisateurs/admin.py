from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "username",
        "nom",
        "prenom",
        "est_evaluateur",
        "is_superuser",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("est_evaluateur",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("est_evaluateur",)}),)


admin.site.register(CustomUser, CustomUserAdmin)
