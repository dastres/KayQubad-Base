from rest_framework import serializers
from blog.models.model_blog_post_category import PostCategory
from blog.api.serializers.serializer_base_category import BaseCategorySerializer


class DetailCategorySerializer(serializers.ModelSerializer):
    parent_category = BaseCategorySerializer(read_only=True)

    class Meta:
        model = PostCategory
        fields = (
            'id', 'title', 'slug', 'description', 'thumbnail', 'thumbnail_alt', 'get_created_at', 'get_updated_at',
            'parent_category', 'status',

        )
        read_only_fields = ('id', 'get_created_at', 'get_updated_at')
