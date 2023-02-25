import tempfile
from django.contrib.auth import get_user_model
from django.test import TestCase

from portfolio.models import Portfolio, PortfolioGallery, PortfolioCategory


class GalleryModelTestCase(TestCase):
    def setUp(self) -> None:
        self.category = PortfolioCategory.objects.create(
            title='sub category fake',
            description='sub description fake',
        )

        self.author = get_user_model().objects.create(
            username='author',
            password='author123'
        )

        self.portfolio = Portfolio.objects.create(
            title='portfolio fake',
            content='content fake',
            author=self.author,
            category=self.category,
        )

        self.obj = PortfolioGallery.objects.create(
            portfolio=self.portfolio,
            title='gallery fake',
        )
        self.obj.image = tempfile.NamedTemporaryFile(suffix='.jpg').name
        self.obj.save()

    def test_str_method(self):
        self.assertIsNotNone(self.obj)
        self.assertEqual(str(self.obj), 'portfolio fake')

    def test_auto_generate_image_alt(self):
        self.assertTrue(self.obj.image_alt)
        self.assertEquals(self.obj.image_alt, 'gallery-fake')

    def test_fields_model(self):
        self.assertTrue(self.obj.image)
        self.assertEquals(self.obj.title, 'gallery fake')
        self.assertEquals(self.obj.portfolio, self.portfolio)
