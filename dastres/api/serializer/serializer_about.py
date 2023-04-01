from rest_framework import serializers
from dastres.models import About


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = (
            'id', 'name', 'position', 'avatar','is_active'
        )
