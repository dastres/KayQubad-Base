from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters

from dastres.models import About
from dastres.api.serializer import AboutListDetailSerializer


class AboutViewSet(viewsets.ModelViewSet):
    model = About
    serializer_class = AboutListDetailSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action in ['list','retrive']:
            return self.serializer_class

    def get_permissions(self):
        if self.action in ('create', 'update', 'destroy', 'partial'):
            return [permissions.IsAdminUser()]
        return super().get_permissions()
