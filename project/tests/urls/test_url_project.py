from django.test import SimpleTestCase
from django.urls import reverse, resolve

from project.api.viewset import ProjectViewSet


class ProjectUrlTestCase(SimpleTestCase):
    def test_app_name(self):
        self.assertIsNotNone(resolve('/fa/api/v1/project/').app_name)
        self.assertEquals(resolve('/fa/api/v1/project/').app_name, 'project')

    def test_portfolio_url_list_create(self):
        path = reverse('project:project-list')
        self.assertEquals(resolve(path).func.__name__, ProjectViewSet.__name__)

    def test_portfolio_url_detail_update_delete(self):
        path = reverse('project:project-detail', kwargs={'pk': 1})
        self.assertEquals(resolve(path).func.__name__, ProjectViewSet.__name__)
