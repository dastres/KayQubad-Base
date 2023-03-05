from rest_framework import serializers

from accounts.api.serializers import BaseUserSerializer
from service.models import Service


class ServiceListSerializer(serializers.ModelSerializer):
    author = BaseUserSerializer()

    class Meta:
        model = Service
        fields = (
            'id', 'title', 'short_description', 'slug', 'author',
            'thumbnail', 'thumbnail_alt', 'is_active', 'status',
            'position', 'is_landing', 'get_created_at', 'get_updated_at'
        )
