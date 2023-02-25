from django.test import SimpleTestCase
from django.urls import reverse, resolve

from portfolio.api.viewset import PortfolioCategoryViewSet


class CategoryUrlTestCase(SimpleTestCase):
    def test_app_name(self):
        self.assertIsNotNone(resolve('/fa/api/v1/portfolio/category/').app_name)
        self.assertEquals(resolve('/fa/api/v1/portfolio/category/').app_name, 'portfolio')

    def test_category_url_list_create(self):
        path = reverse('portfolio:portfolio_category-list')
        self.assertEquals(resolve(path).func.__name__, PortfolioCategoryViewSet.__name__)

    def test_category_url_detail_update_delete(self):
        path = reverse('portfolio:portfolio_category-detail', kwargs={'pk': 1})
        self.assertEquals(resolve(path).func.__name__, PortfolioCategoryViewSet.__name__)
