from rest_framework import serializers
from dastres.models import TeamMembers


class TeamMembersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMembers
        fields = (
            'id', 'name', 'position', 'avatar', 'is_active'
        )
