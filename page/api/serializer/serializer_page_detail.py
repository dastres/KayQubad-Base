from rest_framework import serializers

from page.models.model_page import Page


class PageDetailSerializer(serializers.ModelSerializer):
    # author = UserBaseSerializer() Todo:uncomment After writing

    class Meta:
        model = Page
        fields = ('meta_title','meta_description',"id", 'title', 'content', 'slug', 'thumbnail', 'thumbnail_alt', 'get_created_at', 'get_updated_at', 'status',
                  'is_active', 'custom_template',)
        read_only_fields = ['id', 'get_created_at', 'get_updated_at']
