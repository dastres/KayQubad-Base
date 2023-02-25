from django.test import SimpleTestCase
from django.urls import reverse, resolve

from portfolio.api.viewset import PortfolioViewSet


class PortfolioUrlTestCase(SimpleTestCase):
    def test_app_name(self):
        self.assertIsNotNone(resolve('/fa/api/v1/portfolio/').app_name)
        self.assertEquals(resolve('/fa/api/v1/portfolio/').app_name, 'portfolio')

    def test_portfolio_url_list_create(self):
        path = reverse('portfolio:portfolio-list')
        self.assertEquals(resolve(path).func.__name__, PortfolioViewSet.__name__)

    def test_portfolio_url_detail_update_delete(self):
        path = reverse('portfolio:portfolio-detail', kwargs={'pk': 1})
        self.assertEquals(resolve(path).func.__name__, PortfolioViewSet.__name__)
