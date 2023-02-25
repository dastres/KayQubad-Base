from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.api import viewset


# --------------------------------- Post ------------------------------------------------------
class PostUrlTestCase(SimpleTestCase):
    def test_app_name(self):
        self.assertTrue(resolve('/fa/api/v1/blog/post/').app_name)
        self.assertEqual(resolve('/fa/api/v1/blog/post/').app_name, 'blog')

    def test_create_list_post(self):
        url = reverse('blog:post-list')
        self.assertEqual(resolve(url).func.__name__, viewset.PostViewSet.__name__)
        self.assertNotEqual(resolve(url).func.__name__, viewset.CategoryViewSet.__name__)

    def test_detail_update_delete_post(self):
        url = reverse('blog:post-detail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.__name__, viewset.PostViewSet.__name__)
        self.assertNotEqual(resolve(url).func.__name__, viewset.CategoryViewSet.__name__)
