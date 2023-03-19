from rest_framework import viewsets, status, filters, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from blog.models.model_blog_post import Post

from blog.api.serializers.serializer_list_post import ListPostSerializer
from blog.api.serializers.serializer_detail_post import DetailPostSerializer
from blog.api.serializers.serializer_create_update_post import CreateUpdatePostSerializer


class PostViewSet(viewsets.ModelViewSet):
    model = Post
    lookup_field = 'pk'

    serializer_class = DetailPostSerializer
    permission_classes = [permissions.AllowAny]  # TODO:change to custom permission
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['title', 'slug', 'author__username', 'category__title', 'category__slug']
    filterset_fields = ['title', 'slug', 'category__title', 'category__slug', 'author__username']

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset.order_by('-created_at')

    def get_serializer_class(self):
        if self.action == 'list':
            return ListPostSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return CreateUpdatePostSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action in ['update', 'partial', 'destroy', 'create']:
            return [permissions.IsAdminUser()]
        return super().get_permissions()
