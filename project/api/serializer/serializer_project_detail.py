# 3rd Party
from rest_framework import serializers

# My App
from accounts.api.serializers.serializer_base_user import BaseUserSerializer

from project.models.model_project import Project
from project.api.serializer.serializer_base_project_category import BaseCategorySerializer


class ProjectDetailSerializer(serializers.ModelSerializer):
    author = BaseUserSerializer()
    category = BaseCategorySerializer()

    class Meta:
        model = Project
        fields = [
            'id', 'title', 'content', 'category', 'author', 'slug', 'thumbnail', 'thumbnail_alt', 'status',
            'is_active','meta_title','meta_description',
            'get_created_at', 'get_updated_at',

        ]
        read_only_fields = ['id', 'author', 'created_at', 'updated_at']
