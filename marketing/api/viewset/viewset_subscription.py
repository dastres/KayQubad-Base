from rest_framework import filters
from rest_framework import viewsets
from rest_framework import permissions

from django_filters.rest_framework import DjangoFilterBackend

from marketing.models.model_subscription import EmailSubscription
from marketing.api.serializer.serializer_subscription_create_update import EmailSubscriptionCreateUpdateSerializer
from marketing.api.serializer.serializer_subscription_list_detail import EmailSubscriptionListDetailSerializer


class EmailSubscriptionViewSet(viewsets.ModelViewSet):
    model = EmailSubscription
    serializer_class = EmailSubscriptionListDetailSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]

    search_fields = ['email']
    filterset_fields = ['email']

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return EmailSubscriptionListDetailSerializer
        if self.action in ['create', 'update', 'partial_update']:
            return EmailSubscriptionCreateUpdateSerializer
        return self.serializer_class
