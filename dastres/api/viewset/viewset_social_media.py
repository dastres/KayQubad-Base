from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters

from dastres.models import SocialMedia
from dastres.api.serializer import (
    SocialMediaCreateUpdateSerializer,
    SocialMediaDetailSerializer,
    SocialMediaListSerializer
)


class SocialMediaViewSet(viewsets.ModelViewSet):
    model = SocialMedia
    serializer_class = SocialMediaDetailSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return SocialMediaListSerializer
        elif self.action in ['create','update','partial']:
            return SocialMediaCreateUpdateSerializer
        return self.serializer_class

    def get_permissions(self):
        if self.action in ('create', 'update', 'destroy', 'partial'):
            return [permissions.IsAdminUser()]
        return super().get_permissions()
