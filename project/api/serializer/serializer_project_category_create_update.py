# 3rd Party
from rest_framework import serializers

# My App
from project.models.model_project_category import ProjectCategory


class CategoryCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectCategory
        fields = [
            'id', 'meta_title', 'meta_description', 'title',
            'description', 'slug', 'sub_category', 'thumbnail',
            'thumbnail_alt', 'status', 'is_active', 'get_created_at',
            'get_updated_at'
        ]
        read_only_fields = ['id', 'author', 'get_created_at', 'get_updated_at']
