from rest_framework import serializers

from page.models.model_page import Page


class PageCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ('meta_title','meta_description','title', 'content', 'slug', 'thumbnail', 'thumbnail_alt', 'status', 'is_active', 'custom_template',)
