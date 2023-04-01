from rest_framework import serializers
from dastres.models import TeamMembers
from dastres.api.serializer.serializer_base_social_media import SocialMediaBaseSerializer


class TeamMembersDetailSerializer(serializers.ModelSerializer):
    socials = SocialMediaBaseSerializer(many=True)

    class Meta:
        model = TeamMembers
        fields = (
            'id', 'name', 'position', 'avatar', 'socials', 'is_active'
        )
