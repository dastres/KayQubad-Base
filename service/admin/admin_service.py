from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from service.models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'slug', 'position', 'is_landing', 'created_at', 'updated_at')
    search_fields = ('id', 'title', 'author', 'slug',)
    list_filter = ('position', 'is_landing', 'author',)
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        (_('En'), {'fields': ('title_en', 'content_en', 'short_description_en', 'is_active_en')}),
        (_('Fa'), {'fields': ('title_fa', 'content_fa', 'short_description_fa', 'is_active_fa')}),
        (_('Main'),
         {'fields': ('author', 'slug', 'thumbnail', 'thumbnail_alt', 'is_landing', 'short_description', "position")}),
        (_("Seo information"), {'fields': ("meta_title", "meta_description")}),
        (_('Date'), {'classes': ('collapse',), 'fields': ('created_at', 'updated_at')}),
        (_('Setting'), {'classes': ('collapse',), 'fields': ('status',)})
    )

    add_fieldsets = (
        (_('En'), {'fields': ('title_en', 'content_en', 'short_description_en', 'is_active_en')}),
        (_('Fa'), {'fields': ('title_fa', 'content_fa', 'short_description_fa', 'is_active_fa')}),
        (_('Main'),
         {'fields': ('author', 'slug', 'thumbnail', 'thumbnail_alt', 'is_landing', 'short_description', "position")}),
        (_("Seo information"), {'fields': ("meta_title", "meta_description")}),
        (_('Setting'), {'classes': ('collapse',), 'fields': ('status',)})
    )

