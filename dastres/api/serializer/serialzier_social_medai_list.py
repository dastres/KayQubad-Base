from rest_framework import serializers

from dastres.api.serializer import TeamMemberBaseSerializer
from dastres.models import SocialMedia


class SocialMediaListSerializer(serializers.ModelSerializer):
    team_members = TeamMemberBaseSerializer()

    class Meta:
        model = SocialMedia
        fields = (
            'id', 'title', 'url','team_members','is_active', 'status'
        )
