from django.contrib.auth import get_user_model
from django.test import TestCase
from portfolio.models import Portfolio, PortfolioCategory


class PortfolioModelTestCase(TestCase):
    def setUp(self) -> None:
        self.category = PortfolioCategory.objects.create(
            title='sub category fake',
            description='sub description fake',
        )

        self.author = get_user_model().objects.create(
            username='author',
            password='author123'
        )

        self.obj = Portfolio.objects.create(
            title='portfolio fake',
            content='content fake',
            author=self.author,
            category=self.category,
        )

    def test_method_str(self):
        self.assertEquals(str(self.obj), 'portfolio fake')
        self.assertNotEquals(str(self.obj), 'sub category fake')

    def test_auto_generate_slug(self):
        self.assertTrue(self.obj.slug)
        self.assertEquals(self.obj.slug, 'portfolio-fake')
        self.assertNotEquals(self.obj.slug, 'sub-category-fake')

    def test_auto_generate_thumbnail_alt(self):
        self.assertTrue(self.obj.thumbnail_alt)
        self.assertEquals(self.obj.thumbnail_alt, 'portfolio-fake')
        self.assertNotEquals(self.obj.thumbnail_alt, 'sub-category-fake')

    def test_fields_model_category(self):
        self.assertTrue(self.obj.created_at)
        self.assertEquals(self.obj.content, 'content fake')
        self.assertIsNotNone(self.obj.status)
        self.assertIsNotNone(self.obj.is_active)


