from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters

from dastres.models import TeamMembers
from dastres.api.serializer import TeamMembersCreateUpdateSerializer,TeamMembersDetailSerializer


class TeamMembersViewSet(viewsets.ModelViewSet):
    model = TeamMembers
    serializer_class = TeamMembersCreateUpdateSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action == 'retrive':
            return TeamMembersDetailSerializer
        return self.serializer_class

    # def get_permissions(self):
    #     if self.action in ('create', 'update', 'destroy', 'partial'):
    #         return [permissions.IsAdminUser()]
    #     return super().get_permissions()
