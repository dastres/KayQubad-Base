from django.contrib import admin
from blog.models.model_blog_post_comment import PostComment


@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    list_display = ('post', "name", 'email', 'reply', 'status',)
    search_fields = ('post', 'name', 'email')

    fieldsets = (
        (None, {'fields': ('post', "status")}),
        ("Info User", {'fields': ('name', 'email')}),
        ('Reply', {'fields': ('reply',)}),
    )

    add_fieldsets = (
        (None, {'fields': ('post', "status")}),
        ("Info User", {'fields': ('name', 'email')}),
        ('Reply', {'fields': ('reply ',)}),
    )
