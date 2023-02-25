from rest_framework import serializers
from blog.models.model_blog_post_category import PostCategory
from blog.api.serializers.serializer_base_category import BaseCategorySerializer


class ListCategorySerializer(serializers.ModelSerializer):
    parent_category = BaseCategorySerializer(read_only=True)
    article_count = serializers.SerializerMethodField(method_name='get_article_count')

    class Meta:
        model = PostCategory
        fields = (
            'id', 'title', 'slug', 'thumbnail', 'thumbnail_alt',
            'status', 'parent_category', 'get_created_at', 'get_updated_at', 'is_active','article_count'
        )
        read_only_fields = ['id', 'get_created_at', 'get_updated_at']

    def get_article_count(self, obj):
        categories = obj.posts.all().count()
        return categories
