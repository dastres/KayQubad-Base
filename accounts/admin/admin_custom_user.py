from django.contrib import admin
from django.contrib.auth import get_user_model


@admin.register(get_user_model())
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_staff', 'is_active', 'is_superuser')
    search_fields = ('id', 'username', 'email')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    readonly_fields = ('date_joined', 'last_login')

    fieldsets = (
        ('Main', {'classes': ('collapse',), 'fields': ('username', 'email', 'password', 'first_name', 'last_name')}),
        ('Permission', {'classes': ('collapse',), 'fields': ('is_staff', 'is_active', 'is_superuser')}),
        ('Date', {'classes': ('collapse',), 'fields': ('date_joined', 'last_login',)}),
    )

    fieldsets_add = (
        ('Main', {'classes': ('collapse',), 'fields': ('username', 'email', 'first_name', 'last_name')}),
        ('Permission', {'classes': ('collapse',), 'fields': ('is_staff', 'is_active', 'is_superuser')}),
        ('Date', {'classes': ('collapse',), 'fields': ('date_joined', 'last_login',)}),
    )