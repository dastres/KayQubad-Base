from rest_framework import routers
from project.api.viewset.viewset_project import ProjectViewSet
from project.api.viewset.viewset_project_category import ProjectCategoryViewSet

router = routers.DefaultRouter()
router.register('project/category', ProjectCategoryViewSet, basename='project_category')
router.register('project', ProjectViewSet, basename='project')

urlpatterns = router.urls
