from rest_framework import routers
from marketing.api import viewset

router = routers.DefaultRouter()
router.register('email-subscription', viewset.EmailSubscriptionViewSet, basename='email_subscription')
router.register('user-comment', viewset.UserCommentViewSet, basename='user_comment')

urlpatterns = router.urls
