# Core django
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

# my app
from project.models.model_project_category import ProjectCategory


# ----------------------------------------------------------------------------------------------------------------------

@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'slug', 'sub_category', 'created_at', 'updated_at')
    search_fields = ('title', 'sub_category', 'slug', 'category')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        (_('En'), {'fields': ('title_en', 'description_en', 'sub_category_en', 'is_active_en')}),
        (_('Fa'), {'fields': ('title_fa', 'description_fa', 'sub_category_fa', 'is_active_fa')}),
        (_('Main'), {'fields': ('slug', 'thumbnail', 'thumbnail_alt')}),
        (_("Seo information"), {'fields': ("meta_title", "meta_description")}),
        (_('Date'), {'classes': ('collapse',), 'fields': ('created_at', 'updated_at')}),
        (_('Setting'), {'classes': ('collapse',), 'fields': ('status',)})
    )

    add_fieldsets = (
        (_('En'), {'fields': ('title_en', 'description_en', 'sub_category_en', 'is_active_en')}),
        (_('Fa'), {'fields': ('title_fa', 'description_fa', 'sub_category_fa', 'is_active_fa')}),
        (_('Main'), {'fields': ('slug', 'thumbnail', 'thumbnail_alt')}),
        (_("Seo information"), {'fields': ("meta_title", "meta_description")}),
        (_('Setting'), {'classes': ('collapse',), 'fields': ('status',)})
    )
