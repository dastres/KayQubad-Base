from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from page.models.model_page import Page


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', "author", 'slug', 'status', 'custom_template', 'created_at', 'updated_at')
    search_fields = ('id', 'title', 'slug', 'author')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        (_('En'), {'fields': ('title_en', 'content_en', 'is_active_en')}),
        (_('Fa'), {'fields': ('title_fa', 'content_fa', 'is_active_fa')}),
        (_("Main"), {'fields': ('slug', 'author', 'thumbnail', 'thumbnail_alt', 'custom_template')}),
        (_("Date"), {'fields': ('created_at', "updated_at")}),
        (_("SEO information"), {'fields': ("meta_title", "meta_description")}),
        (_("Setting"), {'fields': ('status',)}),
    )

    add_fieldsets = (
        (_('En'), {'fields': ('title_en', 'content_en', 'is_active_en')}),
        (_('Fa'), {'fields': ('title_fa', 'content_fa', 'is_active_fa')}),
        (_("Main"), {'fields': ('slug', 'author', 'thumbnail', 'thumbnail_alt', 'custom_template')}),
        (_("SEO information"), {'fields': ("meta_title", "meta_description")}),
        (_("Setting"), {'fields': ('status',)}),
    )
