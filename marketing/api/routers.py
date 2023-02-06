from rest_framework import routers
from marketing.api.viewset.viewset_subscription import EmailSubscriptionViewSet

router = routers.DefaultRouter()
router.register('email-subscription', EmailSubscriptionViewSet, basename='email_subscription')
urlpatterns = router.urls
