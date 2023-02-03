# 3rd Party
from rest_framework import serializers

# My App
from project.models import ProjectCategory


class BaseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectCategory
        fields = ['id', 'title', 'slug', 'categories']
        read_only_fields = ['id', 'author', 'created_at', 'updated_at']
