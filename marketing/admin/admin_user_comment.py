# Core Django
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

# My App
from marketing.models import UserComment


@admin.register(UserComment)
class UserCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'company', 'rate', 'is_active', 'get_created_at')
    search_fields = ('id', 'name', 'company')
    list_filter = ('company', 'rate', 'is_active',)
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        (_("Main_en"), {'fields': ('name_en', 'content_en', 'company_en', 'is_active_en')}),
        (_("Main_en"), {'fields': ('name_fa', 'content_fa', 'company_fa', 'is_active_fa')}),
        (_("Main"), {'fields': ('avatar', 'avatar_alt', 'rate')}),
        (_("Date"), {'fields': ('created_at', "updated_at")}),
    )
    add_fieldsets = (
        (_("Main_en"), {'fields': ('name_en', 'content_en', 'company_en', 'is_active_en')}),
        (_("Main_en"), {'fields': ('name_fa', 'content_fa', 'company_fa', 'is_active_fa')}),
        (_("Main"), {'fields': ('avatar', 'avatar_alt', 'rate')}),
        (_("Date"), {'fields': ('created_at', "updated_at")}),
    )
