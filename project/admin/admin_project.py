# Core Django
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

# My App
from project.models.model_project import Project
from project.admin.admin_inline_project_gallery import ProjectGalleryInline


# ----------------------------------------------------------------------------------------------------------------------

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectGalleryInline, ]
    list_display = ('id','title', 'author', 'slug', 'category', 'created_at', 'updated_at')
    search_fields = ('title', 'author', 'slug', 'category')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        (_('En'), {'fields': ('title_en', 'content_en', 'category_en', 'is_active_en')}),
        (_('Fa'), {'fields': ('title_fa', 'content_fa', 'category_fa', 'is_active_fa')}),
        (_('Main'), {'fields': ('author', 'slug', 'thumbnail', 'thumbnail_alt')}),
        (_("Seo information"), {'fields': ("meta_title", "meta_description")}),
        (_('Date'), {'classes': ('collapse',), 'fields': ('created_at', 'updated_at')}),
        (_('Setting'), {'classes': ('collapse',), 'fields': ('status',)})
    )

    add_fieldsets = (
        (_('En'), {'fields': ('title_en', 'content_en', 'category_en', 'is_active_en')}),
        (_('Fa'), {'fields': ('title_fa', 'content_fa', 'category_fa', 'is_active_fa')}),
        (_('Main'), {'fields': ('author', 'slug', 'thumbnail', 'thumbnail_alt')}),
        (_("Seo information"), {'fields': ("meta_title", "meta_description")}),
        (_('Setting'), {'classes': ('collapse',), 'fields': ('status',)})
    )
