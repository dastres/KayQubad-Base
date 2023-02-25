from django.test import SimpleTestCase
from django.urls import reverse, resolve

from marketing.api import viewset


class UserCommentUrlTestCase(SimpleTestCase):
    def test_app_name(self):
        self.assertIsNotNone(resolve('/fa/api/v1/marketing/user-comment/').app_name)
        self.assertEquals(resolve('/fa/api/v1/marketing/user-comment/').app_name, 'marketing')

    def test_category_url_list_create(self):
        path = reverse('marketing:user_comment-list')
        self.assertEquals(resolve(path).func.__name__, viewset.UserCommentViewSet.__name__)

    def test_category_url_detail_update_delete(self):
        path = reverse('marketing:user_comment-detail', kwargs={'pk': 1})
        self.assertEquals(resolve(path).func.__name__, viewset.UserCommentViewSet.__name__)
