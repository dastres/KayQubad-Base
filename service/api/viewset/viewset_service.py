from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters

from service.models import Service
from service.api.serializer import (
    ServiceListSerializer, ServiceDetailSerializer, ServiceCreateUpdateSerializer
)


class ServiceViewSet(viewsets.ModelViewSet):
    model = Service
    serializer_class = ServiceDetailSerializer
    permission_classes = [permissions.AllowAny]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['id', 'title', 'author__username', 'slug', 'short_description']
    filterset_fields = ['position', 'is_landing', 'author__username', ]

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

    def get_permissions(self):
        if self.action in ['update', 'partial', 'destroy', 'create']:
            return [permissions.IsAdminUser()]
        return super().get_permissions()
