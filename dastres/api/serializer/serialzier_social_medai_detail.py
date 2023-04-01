from rest_framework import serializers
from dastres.models import SocialMedia
from dastres.api.serializer import TeamMemberBaseSerializer

class SocialMediaDetailSerializer(serializers.ModelSerializer):
    team_members = TeamMemberBaseSerializer()
    class Meta:
        model = SocialMedia
        fields = (
            'id', 'title', 'url', 'team_members', 'is_active', 'status'
        )
