# Core Django
from django.contrib import admin

# My App
from marketing.models import UserComment


@admin.register(UserComment)
class UserCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'company', 'rate', 'is_active', 'get_created_at')
    search_fields = ('id', 'name', 'company')
    list_filter = ('company', 'rate', 'is_active',)
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ("Main", {'fields': ('name', 'avatar', 'avatar_alt', 'content', 'company', 'rate')}),
        ("Date", {'fields': ('created_at', "updated_at")}),

    )

    add_fieldsets = (
        ("Main", {'fields': ('name', 'avatar', 'avatar_alt', 'content', 'company', 'rate')}),
        ("Date", {'fields': ('created_at', "updated_at")}),

    )
