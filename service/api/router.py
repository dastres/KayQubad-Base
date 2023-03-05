from rest_framework import routers
from service.api import viewset

router = routers.DefaultRouter()
router.register('', viewset.ServiceViewSet, basename='service')

urlpatterns = router.urls
