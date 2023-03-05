from django import test
from django.contrib.auth import get_user_model
from service.models import Service


class ServiceModelTestCase(test.TestCase):
    def setUp(self) -> None:
        self.author = get_user_model().objects.create(
            username='username author'
        )

        self.service = Service.objects.create(
            title='title service',
            content='content service',
            author=self.author,
            short_description='short description service',
            position='Left',
        )

    def test_str_method(self):
        self.assertTrue(self.service)
        self.assertEqual(str(self.service), 'title service')
        self.assertNotEquals(str(self.service), 'short description service')

    def test_auto_generate_slug(self):
        self.assertTrue(self.service.slug)
        self.assertEqual(self.service.slug, 'title-service')
        self.assertNotEquals(self.service.slug, 'title service')

    def test_auto_generate_thumbnail_alt(self):
        self.assertTrue(self.service.thumbnail_alt)
        self.assertEqual(self.service.thumbnail_alt, 'title-service')
        self.assertNotEquals(self.service.thumbnail_alt, 'title service')

    def test_fields_model(self):
        self.assertTrue(self.service.author)
        self.assertTrue(self.service.updated_at)
        self.assertTrue(self.service.created_at)
        self.assertTrue(self.service.status)

        self.assertFalse(self.service.is_landing)

        self.assertEqual(self.service.content, 'content service')
        self.assertEqual(self.service.short_description, 'short description service')
        self.assertNotEqual(self.service.position, 'Right')
