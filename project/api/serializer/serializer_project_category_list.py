# 3rd Party
from rest_framework import serializers

# My App
from project.models.model_project_category import ProjectCategory
from project.api.serializer.serializer_base_project_category import BaseCategorySerializer


class ListCategorySerializer(serializers.ModelSerializer):
    sub_category = BaseCategorySerializer()

    class Meta:
        model = ProjectCategory
        fields = [
            'id', 'title', 'sub_category', 'slug', 'thumbnail', 'thumbnail_alt', 'status', 'is_active'
            , 'get_created_at', 'get_updated_at', 'get_created_at_jalali',
            'get_updated_at_jalali'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
