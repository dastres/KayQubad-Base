from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters

from marketing.models import UserComment
from marketing.api.serializer import UserCommentSerializer


class UserCommentViewSet(viewsets.ModelViewSet):
    model = UserComment
    serializer_class = UserCommentSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]

    search_fields = ['id', 'name', 'company', 'rate']
    filterset_fields = ['company', 'rate', 'is_active']

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset.order_by('-created_at')

    def get_permissions(self):
        if self.action in ['update', 'partial', 'destroy', 'create']:
            return [permissions.IsAdminUser()]
        return super().get_permissions()
