# from django.contrib import admin
# from .models import SoumissionArticle

# class JournalAdmin(admin.ModelAdmin):
#     readonly_fields = ('created',)

# admin.site.register(SoumissionArticle, JournalAdmin)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        #"email",
        "username",
        "nom",
        "prenom",
        #"age",
        "est_evaluateur",
        "is_superuser",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("age", "est_evaluateur")}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("age", "est_evaluateur")}),)


admin.site.register(CustomUser, CustomUserAdmin)
