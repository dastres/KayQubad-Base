from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework import permissions
from accounts.api.serializers import UserListSerializer, UserDetailSerializer


class UserViewSet(viewsets.ModelViewSet):
    model = get_user_model()
    permissions = [permissions.IsAuthenticated]
    serializer_class = UserDetailSerializer

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return UserListSerializer
        return self.serializer_class
