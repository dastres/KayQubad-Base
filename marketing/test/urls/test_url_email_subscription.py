from django.test import SimpleTestCase
from django.urls import reverse, resolve

from marketing.api import viewset


class EmailSubscriptionUrlTestCase(SimpleTestCase):
    def test_app_name(self):
        self.assertIsNotNone(resolve('/fa/api/v1/marketing/email-subscription/').app_name)
        self.assertEquals(resolve('/fa/api/v1/marketing/email-subscription/').app_name, 'marketing')

    def test_category_url_list_create(self):
        path = reverse('marketing:email_subscription-list')
        self.assertEquals(resolve(path).func.__name__, viewset.EmailSubscriptionViewSet.__name__)

    def test_category_url_detail_update_delete(self):
        path = reverse('marketing:email_subscription-detail', kwargs={'pk': 1})
        self.assertEquals(resolve(path).func.__name__, viewset.EmailSubscriptionViewSet.__name__)
