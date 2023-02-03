from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from blog.models.model_blog_post_comment import PostComment


@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', "name", 'email', 'reply', 'status',)
    search_fields = ('id', 'post', 'name', 'email')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        (_('En'), {'fields': ('name_en', 'message_en', 'post_en', 'reply_en', 'is_active_en')}),
        (_('Fa'), {'fields': ('name_fa', 'message_fa', 'post_fa', 'reply_fa', 'is_active_fa')}),
        (_("Main"), {'fields': ('email',)}),
        (_("Date"), {'fields': ('created_at', "updated_at")}),
        (_("Setting"), {'fields': ('status',)})
    )

    add_fieldsets = (
        (_('En'), {'fields': ('name_en', 'message_en', 'post_en', 'reply_en', 'is_active_en')}),
        (_('Fa'), {'fields': ('name_fa', 'message_fa', 'post_fa', 'reply_fa', 'is_active_fa')}),
        (_("Main"), {'fields': ('email',)}),
        (_("Setting"), {'fields': ('status',)})
    )