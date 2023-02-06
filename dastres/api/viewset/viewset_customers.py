from rest_framework import filters
from rest_framework import viewsets
from rest_framework import permissions

from django_filters.rest_framework import DjangoFilterBackend

from dastres.models.models_customers import Customers
from dastres.api.serializer.serializer_customers import CustomersSerializer

class CustomersViewSet(viewsets.ModelViewSet):
    model = Customers
    serializer_class = CustomersSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]

    search_fields = ['name']
    filterset_fields = ['name']

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset
