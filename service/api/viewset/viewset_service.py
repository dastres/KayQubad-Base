from rest_framework import viewsets

from service.models import Service
from service.api.serializer import (
    ServiceListSerializer, ServiceDetailSerializer, ServiceCreateUpdateSerializer
)


class ServiceViewSet(viewsets.ModelViewSet):
    model = Service
    serializer_class = ServiceDetailSerializer

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return ServiceListSerializer
        elif self.action in ['create', 'update', 'partial']:
            return ServiceCreateUpdateSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)
