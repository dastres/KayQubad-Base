from rest_framework import routers
from dastres.api import viewset

router = routers.DefaultRouter()
router.register('team-member/social', viewset.SocialMediaViewSet, basename='social_media')
router.register('team-member', viewset.TeamMembersViewSet, basename='team_member')
router.register('customers', viewset.CustomersViewSet, basename='customers')
router.register('landing-section', viewset.LandingSectionsViewSet, basename='landing')

urlpatterns = router.urls
