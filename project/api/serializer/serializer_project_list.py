# 3rd Party
from rest_framework import serializers

# My App
from project.models.model_project import Project
from project.api.serializer.serializer_base_project_category import BaseCategorySerializer


class ProjectListSerializer(serializers.ModelSerializer):
    category = BaseCategorySerializer()

    class Meta:
        model = Project
        fields = (
            'id', 'title', 'category', 'slug', 'thumbnail', 'thumbnail_alt', 'get_created_at', 'get_updated_at',
            'meta_title','meta_description',
        )
        read_only_fields = ['id', 'created_at', 'updated_at']
