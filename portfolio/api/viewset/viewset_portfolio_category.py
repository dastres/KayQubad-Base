from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from portfolio.models.model_portfolio_category import PortfolioCategory
from portfolio.api.serializer.serializer_portfolio_category_list import CategoryListSerializer
from portfolio.api.serializer.serializer_portfolio_category_create_update import CategoryCreateUpdateSerializer
from portfolio.api.serializer.serializer_portfolio_category_detail import CategoryDetailSerializer


class PortfolioCategoryViewSet(viewsets.ModelViewSet):
    model = PortfolioCategory
    serializer_class = CategoryDetailSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'slug', 'sub_category__title']
    filterset_fields = ['title', 'slug', 'sub_category__title']

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset.order_by('-created_at')

    def get_serializer_class(self):
        if self.action == 'list':
            return CategoryListSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return CategoryCreateUpdateSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ['update', 'partial', 'destroy', 'create']:
            return [permissions.IsAdminUser()]
        return super().get_permissions()
