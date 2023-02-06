from rest_framework import routers
from dastres.api.viewset.viewset_customers import CustomersViewSet

router = routers.DefaultRouter()
router.register('customers', CustomersViewSet, basename='customers')
urlpatterns = router.urls
