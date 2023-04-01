from rest_framework import serializers
from dastres.models import SocialMedia


class SocialMediaBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ('id', 'title', 'url', 'status', 'is_active')
