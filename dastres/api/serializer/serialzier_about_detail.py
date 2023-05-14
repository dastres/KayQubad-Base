from rest_framework import serializers

from dastres.api.serializer import  TeamMembersDetailSerializer, CustomersSerializer
from dastres.api.serializer.serializer_landing_to_about import LandingToAboutSerializer
from dastres.models import About, TeamMembers, Customers, LandingSections


class AboutDetailSerializer(serializers.ModelSerializer):
    team_members = serializers.SerializerMethodField()
    customers = serializers.SerializerMethodField()
    landing_data = serializers.SerializerMethodField()

    class Meta:
        model = About
        fields = (
            'id', 'cover_video', 'video', 'description', 'customers', 'is_active', 'team_members', 'meta_title',
            'meta_description','landing_data'
        )

    def get_team_members(self, obj):
        query = TeamMembers.objects.all()
        return TeamMembersDetailSerializer(query, many=True).data

    def get_customers(self, obj):
        query = Customers.objects.filter(status=1)[0:3]
        return CustomersSerializer(query, many=True).data

    def get_landing_data(self,obj):
        query = LandingSections.objects.last()
        return LandingToAboutSerializer(query).data
