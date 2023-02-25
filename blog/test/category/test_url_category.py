from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.api import viewset


# --------------------------------- Post ------------------------------------------------------
class CategoryUrlTestCase(SimpleTestCase):
    def test_app_name(self):
        self.assertTrue(resolve('/fa/api/v1/blog/category/').app_name)
        self.assertEqual(resolve('/fa/api/v1/blog/category/').app_name, 'blog')

    def test_create_list_post(self):
        url = reverse('blog:category-list')
        self.assertEqual(resolve(url).func.__name__, viewset.CategoryViewSet.__name__)
        self.assertNotEqual(resolve(url).func.__name__, viewset.PostCommentViewSet.__name__)

    def test_detail_update_delete_post(self):
        url = reverse('blog:category-detail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.__name__, viewset.CategoryViewSet.__name__)
        self.assertNotEqual(resolve(url).func.__name__, viewset.PostCommentViewSet.__name__)