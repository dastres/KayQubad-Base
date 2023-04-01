from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters

from dastres.models import TeamMembers
from dastres.api.serializer import (
    TeamMembersCreateUpdateSerializer,
    TeamMembersDetailSerializer,
    TeamMembersListSerializer
)


class TeamMembersViewSet(viewsets.ModelViewSet):
    model = TeamMembers
    serializer_class = TeamMembersDetailSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return TeamMembersListSerializer
        elif self.action in ['create','update','partial']:
            return TeamMembersCreateUpdateSerializer
        return self.serializer_class

    def get_permissions(self):
        if self.action in ('create', 'update', 'destroy', 'partial'):
            return [permissions.IsAdminUser()]
        return super().get_permissions()
