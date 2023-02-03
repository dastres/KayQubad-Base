from django.contrib import admin
from blog.models.model_blog_post import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', "author", 'slug', 'status', 'created_at', 'updated_at')
    search_fields = ('title', 'slug', 'author')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ("Main", {'fields': ('title', 'slug', 'thumbnail', 'thumbnail_alt', 'author', 'category', 'content')}),
        ("Date", {'fields': ('created_at', "updated_at")}),
        ("SEO information", {'fields': ("meta_title", "meta_description")}),
        ('Settings', {'fields': ('status',)}),
    )

    add_fieldsets = (
        ("Main", {'fields': ('title', 'slug', 'thumbnail', 'thumbnail_alt', 'author', 'category', 'content')}),
        ("SEO Information", {'fields': ("meta_title", "meta_description")}),
        ('Settings', {'fields': ('status',)}),
    )
