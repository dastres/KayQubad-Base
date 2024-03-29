# 3rd Party
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters

# My App
from forms.models import ContactUs
from forms.api.serializer.serializer_list_contact_us import ListContactUsSerializer
from forms.api.serializer.serializer_detail_contact_us import DetailContactUsSerializer
from forms.api.serializer.serializer_create_update_contact_us import CreateUpdateContactUsSerializer


class ContactUsViewSet(viewsets.ReadOnlyModelViewSet):
    model = ContactUs
    lookup_field = 'pk'

    serializer_class = DetailContactUsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['name', 'email', 'phone_number']
    filterset_fields = ['name', 'email', 'phone_number']

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return ListContactUsSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return CreateUpdateContactUsSerializer
        return self.serializer_class
