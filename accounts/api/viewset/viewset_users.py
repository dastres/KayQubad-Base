from rest_framework import viewsets, status
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from accounts import permissions as custom_permission
from accounts.api.serializers import UserListSerializer, UserDetailSerializer, UserCreateSerializer


class UserViewSet(viewsets.ModelViewSet):
    model = get_user_model()
    permissions = [permissions.IsAdminUser()]
    serializer_class = UserDetailSerializer

    @action(detail=False, methods=['get'])
    def profile(self, request):
        user = get_object_or_404(get_user_model(), username=request.user)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return UserListSerializer
        elif self.action == 'create':
            return UserCreateSerializer
        return self.serializer_class

    def get_permissions(self):
        if self.action == 'profile':
            return [custom_permission.IsUser()]
        return self.permissions
