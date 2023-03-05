from rest_framework import viewsets

from service.models import Service
from service.api.serializer import (
    ServiceListSerializer
)


class ServiceViewSet(viewsets.ModelViewSet):
    model = Service
    serializer_class = ServiceListSerializer

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset
