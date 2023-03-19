from rest_framework import filters
from rest_framework import viewsets
from rest_framework import permissions

from django_filters.rest_framework import DjangoFilterBackend

from page.models.model_page import Page
from page.api.serializer.serializer_page_list import PageListSerializer
from page.api.serializer.serializer_page_create_update import PageCreateUpdateSerializer
from page.api.serializer.serializer_page_detail import PageDetailSerializer


class PageViewSet(viewsets.ModelViewSet):
    model = Page
    serializer_class = PageDetailSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]

    search_fields = ['title', 'slug', 'author__username']
    filterset_fields = ['title', 'slug', 'author']

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset.order_by('-created_at')

    def get_serializer_class(self):
        if self.action == 'list':
            return PageListSerializer
        if self.action in ['create', 'update', 'partial_update']:
            return PageCreateUpdateSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action in ['update', 'partial', 'destroy', 'create']:
            return [permissions.IsAdminUser()]
        return super().get_permissions()
