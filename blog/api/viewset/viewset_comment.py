# 3rd Party
from django.core.cache import cache
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response

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
        elif self.action in ['add_like', 'add_dislike']:
            return [permissions.IsAuthenticated()]
        return super().get_permissions()

    @action(detail=True, methods=['post'], name='add-like-comment')
    def add_like(self, request, pk=None):
        comment = cache.get('comment')
        if comment is None:
            comment = PostComment.objects.get(pk=pk)
            cache.set('comment', comment)

        if comment.dislike.filter(id=request.user.id).exists():
            return Response('', status=status.HTTP_400_BAD_REQUEST)

        if comment.likes.filter(id=request.user.id).exists():
            comment.likes.remove(request.user)
            return Response('Like Remove .', status=status.HTTP_200_OK)
        else:
            comment.likes.add(request.user)
            return Response('Like Addd .', status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], name='add-dislike-comment')
    def add_dislike(self, request, pk=None):
        comment = cache.get('comment')
        if comment is None:
            comment = PostComment.objects.get(pk=pk)
            cache.set('comment', comment)

        if comment.likes.filter(id=request.user.id).exists():
            return Response('', status=status.HTTP_400_BAD_REQUEST)

        if comment.dislike.filter(id=request.user.id).exists():
            comment.dislike.remove(request.user)
            return Response('Dislike Remove .', status=status.HTTP_200_OK)
        else:
            comment.dislike.add(request.user)
            return Response('Dislike Add .', status=status.HTTP_200_OK)
