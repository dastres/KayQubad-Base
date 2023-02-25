from rest_framework import serializers
from blog.models.model_blog_post import Post
from blog.api.serializers import BaseCategorySerializer
from accounts.api.serializers import BaseUserSerializer


class DetailPostSerializer(serializers.ModelSerializer):
    category = BaseCategorySerializer(read_only=True)
    author = BaseUserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = (
            'id', 'title', 'content', 'slug', 'thumbnail', 'thumbnail_alt','short_description','study_time',
            'status', 'author', 'category', 'get_created_at', 'get_updated_at','is_active','status'
        )

        read_only_fields = ['id', 'get_created_at', 'get_updated_at']
