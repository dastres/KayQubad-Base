from rest_framework import serializers
from service.models import Service


class ServiceCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = (
            'title', 'short_description', 'slug','content',
            'thumbnail', 'is_active', 'status',
            'position', 'is_landing','meta_title', 'meta_description'
        )
        read_only_fields = ('id', 'created_at', 'updated_at', 'author')
