from django.test import SimpleTestCase
from django.urls import reverse, resolve

from project.api.viewset import ProjectCategoryViewSet


class CategoryUrlTestCase(SimpleTestCase):
    def test_app_name(self):
        self.assertIsNotNone(resolve('/fa/api/v1/project/category/').app_name)
        self.assertEquals(resolve('/fa/api/v1/project/category/').app_name, 'project')

    def test_category_url_list_create(self):
        path = reverse('project:project_category-list')
        self.assertEquals(resolve(path).func.__name__, ProjectCategoryViewSet.__name__)

    def test_category_url_detail_update_delete(self):
        path = reverse('project:project_category-detail', kwargs={'pk': 1})
        self.assertEquals(resolve(path).func.__name__, ProjectCategoryViewSet.__name__)
