from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin
from blog.models.model_blog_post import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', "author", 'slug', 'status', 'created_at', 'updated_at')
    search_fields = ('id', 'title', 'slug', 'author')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        (_('En'), {'fields': ('title_en', 'content_en', 'category_en', 'status_en', 'is_active_en')}),
        (_('Fa'), {'fields': ('title_fa', 'content_fa', 'category_fa', 'status_fa', 'is_active_fa')}),
        (_("Main"), {'fields': ('slug', 'author', 'thumbnail', 'thumbnail_alt')}),
        (_("Date"), {'fields': ('created_at', "updated_at")}),
        (_("SEO information"), {'fields': ("meta_title", "meta_description")}),
    )

    add_fieldsets = (
        (_('En'), {'fields': ('title_en', 'content_en', 'category_en', 'status_en', 'is_active_en')}),
        (_('Fa'), {'fields': ('title_fa', 'content_fa', 'category_fa', 'status_fa', 'is_active_fa')}),
        (_("Main"), {'fields': ('slug', 'author', 'thumbnail', 'thumbnail_alt')}),
        (_("SEO information"), {'fields': ("meta_title", "meta_description")}),
    )
