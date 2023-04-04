from rest_framework import serializers

from dastres.api.serializer import TeamMembersDetailSerializer,CustomersSerializer
from dastres.models import About, TeamMembers,Customers


class AboutDetailSerializer(serializers.ModelSerializer):
    team_members = serializers.SerializerMethodField()
    customers = serializers.SerializerMethodField()

    class Meta:
        model = About
        fields = (
            'id', 'cover_video', 'video', 'description','customers', 'is_active', 'team_members','meta_title','meta_description'
        )

    def get_team_members(self, obj):
        query = TeamMembers.objects.all()
        return TeamMembersDetailSerializer(query, many=True).data

    def get_customers(self, obj):
        query = Customers.objects.filter(status=1)[0:3]
        return CustomersSerializer(query, many=True).data

