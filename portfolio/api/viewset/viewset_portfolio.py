from rest_framework import filters
from rest_framework import viewsets
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend

from portfolio.models.model_portfolio import Portfolio
from portfolio.api.serializer.serializer_portfolio_list import PortfolioListSerializer
from portfolio.api.serializer.serializer_portfolio_detail import PortfolioDetailSerializer
from portfolio.api.serializer.serializer_portfolio_create_update import PortfolioCreateUpdateSerializer


class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioDetailSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'slug', 'author__username', 'category__title', 'category__slug']
    filterset_fields = ['title', 'slug', 'category__title', 'category__slug', 'author__username']

    def get_serializer_class(self):
        if self.action == 'list':
            return PortfolioListSerializer
        elif self.action in ['update', 'create', 'partial_update']:
            return PortfolioCreateUpdateSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action in ['update', 'partial', 'destroy', 'create']:
            return [permissions.IsAdminUser()]
        return super().get_permissions()
