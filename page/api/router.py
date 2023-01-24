from rest_framework import routers
from page.api.viewset.viewset_page import PageViewSet

router = routers.DefaultRouter()
router.register('page', PageViewSet, basename='page')
urlpatterns = router.urls
