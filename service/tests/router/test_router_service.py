from django.test import SimpleTestCase
from django.urls import reverse, resolve

from service.models import Service
from service.api import viewset


class ServiceRouterTestCase(SimpleTestCase):
    def test_app_name(self):
        self.assertIsNotNone(resolve('/fa/api/v1/service/').app_name)
        self.assertEquals(resolve('/fa/api/v1/service/').app_name, 'service')

    def test_service_url_list_create(self):
        path = reverse('service:service-list')
        self.assertEquals(resolve(path).func.__name__, viewset.ServiceViewSet.__name__)

    def test_service_url_detail_update_delete(self):
        path = reverse('service:service-detail', kwargs={'slug': 'slug-test'})
        self.assertEquals(resolve(path).func.__name__, viewset.ServiceViewSet.__name__)
