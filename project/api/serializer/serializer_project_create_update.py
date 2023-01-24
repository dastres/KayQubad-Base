# 3rd Party
from rest_framework import serializers

# My App
from project.models.model_project import Project


class ProjectCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            'id', 'meta_title', 'meta_description','title','content','slug','author','thumbnail','thumbnail_alt',
            'get_created_at','get_updated_at','status','is_active','category'
        )
        read_only_fields = ['id','author','created_at', 'updated_at']
