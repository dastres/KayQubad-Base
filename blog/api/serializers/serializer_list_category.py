from rest_framework import serializers
from blog.models.model_blog_post_category import PostCategory
from blog.api.serializers.serializer_base_category import BaseCategorySerializer


class ListCategorySerializer(serializers.ModelSerializer):
    parent_category = BaseCategorySerializer(read_only=True)

    class Meta:
        model = PostCategory
        fields = (
            'id', 'title', 'slug', 'thumbnail', 'thumbnail_alt',
            'status', 'parent_category', 'get_created_at', 'get_updated_at', 'is_active'
        )
        read_only_fields = ['id', 'get_created_at', 'get_updated_at']
