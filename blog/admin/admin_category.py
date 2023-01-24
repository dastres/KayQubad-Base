from django.contrib import admin
from blog.models.model_blog_post_category import PostCategory


@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', "parent_category", 'slug', 'status', 'created_at', 'updated_at')
    search_fields = ('title', 'slug', 'parent_category')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ("Main", {'fields': ('title', 'slug', 'thumbnail', 'thumbnail_alt', 'description')}),
        ('Sub Category', {'fields': ('parent_category',)}),
        ("Date", {'fields': ('created_at', "updated_at")}),
        ("SEO Information", {'fields': ("meta_title", "meta_description")}),
        ('Settings', {'fields': ('status',)}),
    )

    add_fieldsets = (
        ("Main", {'fields': ('title', 'slug', 'thumbnail', 'thumbnail_alt', 'description')}),
        ('Sub Category', {'fields': ('parent_category',)}),
        ("SEO Information", {'fields': ("meta_title", "meta_description")}),
        ('Settings', {'fields': ('status',)}),
    )
