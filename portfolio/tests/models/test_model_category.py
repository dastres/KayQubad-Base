from django.test import TestCase
from portfolio.models import PortfolioCategory


class CategoryModelTestCase(TestCase):
    def setUp(self) -> None:
        self.sub_category = PortfolioCategory.objects.create(
            title='sub category fake',
            description='sub description fake',
        )

        self.category = PortfolioCategory.objects.create(
            title='category fake',
            description='description fake',
            sub_category=self.sub_category
        )

    def test_method_str(self):
        self.assertEquals(str(self.category), 'category fake')
        self.assertEquals(str(self.sub_category), 'sub category fake')

        self.assertNotEquals(str(self.sub_category), 'category fake')
        self.assertNotEquals(str(self.category), 'sub category fake')

    def test_auto_generate_slug(self):
        self.assertTrue(self.category.slug)
        self.assertTrue(self.sub_category.slug)

        self.assertEquals(self.category.slug, 'category-fake')
        self.assertEquals(self.sub_category.slug, 'sub-category-fake')

    def test_auto_generate_thumbnail_alt(self):
        self.assertTrue(self.category.thumbnail_alt)
        self.assertTrue(self.sub_category.thumbnail_alt)

        self.assertEquals(self.category.thumbnail_alt, 'category-fake')
        self.assertEquals(self.sub_category.thumbnail_alt, 'sub-category-fake')

    def test_fields_model_category(self):
        self.assertTrue(self.category.created_at)
        self.assertEquals(self.category.description, 'description fake')
        self.assertIsNotNone(self.category.status)
        self.assertIsNotNone(self.category.is_active)

    def test_fields_model_sub_category(self):
        self.assertTrue(self.sub_category.created_at)
        self.assertEquals(self.sub_category.description, 'sub description fake')
        self.assertIsNotNone(self.sub_category.status)
        self.assertIsNotNone(self.sub_category.is_active)
