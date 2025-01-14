from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Customize fields to display in the admin interface
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('profile_picture', 'bio')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('profile_picture', 'bio')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
