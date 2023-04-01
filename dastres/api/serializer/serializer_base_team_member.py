from rest_framework import serializers
from dastres.models import TeamMembers


class TeamMemberBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMembers
        fields = ('id', 'name',)
