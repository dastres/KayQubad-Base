from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters
from marketing.models import UserComment


class UserCommentViewSet(viewsets.ModelViewSet):
    model = UserComment
    serializer_class = EmailSubscriptionListDetailSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]

    search_fields = ['id', 'name', 'company', 'rate']
    filterset_fields = ['company', 'rate', 'is_active']

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return EmailSubscriptionListDetailSerializer
        if self.action in ['create', 'update', 'partial_update']:
            return EmailSubscriptionCreateUpdateSerializer
        return self.serializer_class
