from rest_framework import routers
from dastres.api import viewset

router = routers.DefaultRouter()
router.register('customers', viewset.CustomersViewSet, basename='customers')
router.register('landing-section', viewset.LandingSectionsViewSet, basename='landing')

urlpatterns = router.urls
