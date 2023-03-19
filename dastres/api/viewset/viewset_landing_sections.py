from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters

from dastres.models import LandingSections
from dastres.api.serializer import LandingSectionsSerializer


class LandingSectionsViewSet(viewsets.ModelViewSet):
    model = LandingSections
    serializer_class = LandingSectionsSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset.order_by('-created_at')

    def get_permissions(self):
        if self.action in ('create', 'update', 'destroy', 'partial'):
            return [permissions.IsAdminUser()]
        return super().get_permissions()
