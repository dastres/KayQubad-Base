from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from blog.models.model_blog_post_category import PostCategory


@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', "parent_category", 'slug', 'status', 'created_at', 'updated_at')
    search_fields = ('id', 'title', 'slug', 'parent_category')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        (_('En'), {'fields': ('title_en', 'description_en', 'parent_category_en', 'status_en', 'is_active_en')}),
        (_('Fa'), {'fields': ('title_fa', 'description_fa', 'parent_category_fa', 'status_fa', 'is_active_fa')}),
        (_("Main"), {'fields': ('slug', 'thumbnail', 'thumbnail_alt')}),
        (_("Date"), {'fields': ('created_at', "updated_at")}),
        (_("SEO information"), {'fields': ("meta_title", "meta_description")}),
    )

    add_fieldsets = (
        (_('En'), {'fields': ('title_en', 'description_en', 'parent_category_en', 'status_en', 'is_active_en')}),
        (_('Fa'), {'fields': ('title_fa', 'description_fa', 'parent_category_fa', 'status_fa', 'is_active_fa')}),
        (_("Main"), {'fields': ('slug', 'thumbnail', 'thumbnail_alt')}),
        (_("SEO information"), {'fields': ("meta_title", "meta_description")}),
    )
