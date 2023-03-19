from rest_framework import serializers

from page.models.model_page import Page


class PageListSerializer(serializers.ModelSerializer):
    # author = UserBaseSerializer()

    class Meta:
        model = Page
        fields = ['meta_title','meta_description','id', 'title', 'slug', 'author', 'custom_template', 'is_active', 'get_created_at', 'get_updated_at']
        read_only_fields = ['id', 'get_created_at', 'get_updated_at']
