# Core Django
from django.contrib import admin

# My App
from marketing.models import UserComment


@admin.register(UserComment)
class UserCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'company', 'rate', 'is_active', 'get_created_at')
    search_fields = ('id', 'name', 'company')
    list_filter = ('company', 'rate', 'is_active',)
