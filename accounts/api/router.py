from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from accounts.api import viewset

router = routers.DefaultRouter()
router.register('users', viewset.UserViewSet, basename='users')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/change_password/', viewset.ChangePasswordViewSet.as_view(), name='user_change_password'),
    path('', include(router.urls))
]
