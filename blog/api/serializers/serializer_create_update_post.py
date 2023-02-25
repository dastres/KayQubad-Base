from rest_framework import serializers
from blog.models.model_blog_post import Post


class CreateUpdatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title', 'content', 'short_description', 'slug', 'thumbnail', 'thumbnail_alt', 'category', 'is_active'
        )
