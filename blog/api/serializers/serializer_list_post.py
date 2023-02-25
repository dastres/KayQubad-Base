from rest_framework import serializers

from blog.models.model_blog_post import Post
from accounts.api.serializers import BaseUserSerializer
from blog.api.serializers import BaseCategorySerializer


class ListPostSerializer(serializers.ModelSerializer):
    author = BaseUserSerializer(read_only=False)
    category = BaseCategorySerializer(read_only=False)

    class Meta:
        model = Post
        fields = (
            'id', 'title', 'slug', 'thumbnail', 'thumbnail_alt','short_description',
            'status', 'author', 'category', 'get_created_at', 'get_updated_at','is_active','status'
        )
