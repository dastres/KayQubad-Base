# 3rd Party
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

# My App
from project.models.model_project_category import ProjectCategory
from project.api.serializer.serializer_project_category_list import ListCategorySerializer
from project.api.serializer.serializer_project_category_detail import CategoryDetailSerializer
from project.api.serializer.serializer_project_category_create_update import CategoryCreateUpdateSerializer


class ProjectCategoryViewSet(viewsets.ModelViewSet):
    model = ProjectCategory
    serializer_class = CategoryDetailSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'slug', 'sub_category__title']
    filterset_fields = ['title', 'slug', 'sub_category__title']

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return ListCategorySerializer
        elif self.action in ['create', 'update', 'partial']:
            return CategoryCreateUpdateSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ['update', 'partial', 'destroy', 'create']:
            return [permissions.IsAdminUser()]
        return super().get_permissions()
