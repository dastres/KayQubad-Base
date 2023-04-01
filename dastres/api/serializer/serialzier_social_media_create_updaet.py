from rest_framework import serializers
from dastres.models import SocialMedia


class SocialMediaCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = (
            'id', 'title', 'url', 'team_members', 'is_active', 'status'
        )
