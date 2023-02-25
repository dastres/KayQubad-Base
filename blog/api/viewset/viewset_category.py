from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, permissions

from blog.models.model_blog_post_category import PostCategory

from blog.api.serializers.serializer_list_category import ListCategorySerializer
from blog.api.serializers.serializer_create_update_category import CreateUpdateCategorySerializer
from blog.api.serializers.serializer_detail_category import DetailCategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    model = PostCategory
    lookup_field = 'pk'

    permission_classes = [permissions.AllowAny]
    serializer_class = DetailCategorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['title', 'slug', 'parent_category__title']
    filterset_fields = ['title', 'slug', 'parent_category__title']

    def get_queryset(self):
        queryset = PostCategory.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return ListCategorySerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return CreateUpdateCategorySerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ['update', 'partial', 'destroy', 'create']:
            return [permissions.IsAdminUser()]
        return super().get_permissions()
