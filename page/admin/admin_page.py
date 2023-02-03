from django.contrib import admin
from page.models.model_page import Page


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'custom_template', 'slug', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'slug', 'author')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Main', {'fields': ('title', 'slug', 'author', 'content', 'custom_template')}),
        ("Seo information", {'fields': ("meta_title", "meta_description")}),
        ('Date', {'classes': ('collapse',), 'fields': ('created_at', 'updated_at')})
    )

    add_fieldsets = (
        ('Main', {'fields': ('title', 'slug', 'author', 'content', 'custom_template')}),
        ("Seo information", {'fields': ("meta_title", "meta_description")}),
    )
