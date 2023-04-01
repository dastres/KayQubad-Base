from rest_framework import serializers
from dastres.models import TeamMembers


class TeamMembersCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMembers
        fields = (
            'id', 'name', 'position', 'avatar', 'is_active'
        )
