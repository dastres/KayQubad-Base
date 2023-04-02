from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.generics import UpdateAPIView

from accounts.api.serializers import ChangePasswordSerializer


class ChangePasswordViewSet(UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'password change'}, status=status.HTTP_200_OK)