from rest_framework import serializers

from accounts.api.serializers import BaseUserSerializer
from service.models import Service


class ServiceDetailSerializer(serializers.ModelSerializer):
    author = BaseUserSerializer()

    class Meta:
        model = Service
        fields = (
            'id', 'title', 'short_description', 'slug', 'author', 'content',
            'thumbnail', 'thumbnail_alt', 'is_active', 'status',
            'position', 'is_landing', 'get_created_at', 'get_updated_at',
            'meta_title', 'meta_description'
        )
        read_only_fields = ('id', 'created_at', 'updated_at', 'author')
