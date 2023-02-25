# 3rd Party
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters

# My App
from blog.models import PostComment
from blog.api.serializers.serializer_create_update_comment import CreateUpdateCommentSerializer
from blog.api.serializers.serializer_list_comment import ListCommentSerializer
from blog.api.serializers.serializer_detail_comment import DetailCommentSerializer


class PostCommentViewSet(viewsets.ModelViewSet):
    model = PostComment
    lookup_field = 'pk'

    serializer_class = DetailCommentSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['name', 'email', 'post__title', 'post__slug', 'reply__name', 'reply__email']
    filterset_fields = ['name', 'email', 'post__title', 'post__slug', 'reply__name', 'reply__email']

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CreateUpdateCommentSerializer
        elif self.action == 'list':
            return ListCommentSerializer
        return self.serializer_class

    def get_permissions(self):
        if self.action in ['update', 'partial', 'destroy']:
            return [permissions.IsAdminUser()]
        elif self.action == 'create':
            return [permissions.IsAuthenticated()]
        return super().get_permissions()
