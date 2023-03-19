from rest_framework import serializers
from blog.models.model_blog_post_category import PostCategory
from blog.api.serializers.serializer_base_category import BaseCategorySerializer


class CreateUpdateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PostCategory
        fields = (
            'meta_title','meta_description','title', 'slug', 'description', 'thumbnail', 'thumbnail_alt', 'parent_category', 'status', 'is_active'

        )
