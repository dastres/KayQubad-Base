# 3rd Party
from rest_framework import serializers

# My App
from project.models.model_project_category import ProjectCategory
from project.api.serializer.serializer_base_project_category import BaseCategorySerializer


class CategoryDetailSerializer(serializers.ModelSerializer):
    sub_category = BaseCategorySerializer()

    class Meta:
        model = ProjectCategory
        fields = ['id', 'meta_title', 'meta_description', 'title', 'description', 'slug', 'sub_category', 'thumbnail',
                  'thumbnail_alt', 'status', 'is_active', 'get_created_at', 'get_updated_at'
                  ]
        read_only_fields = ['id', 'author', 'created_at', 'updated_at']
