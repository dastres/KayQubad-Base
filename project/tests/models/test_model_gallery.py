import tempfile
from django.contrib.auth import get_user_model
from django.test import TestCase

from project.models import Project, ProjectCategory, ProjectGallery


class GalleryModelTestCase(TestCase):
    def setUp(self) -> None:
        self.category = ProjectCategory.objects.create(
            title='sub category fake',
            description='sub description fake',
        )

        self.author = get_user_model().objects.create(
            username='author',
            password='author123'
        )

        self.project = Project.objects.create(
            title='project fake',
            content='content fake',
            author=self.author,
            category=self.category,
        )

        self.obj = ProjectGallery.objects.create(
            project=self.project,
            title='gallery fake',
        )
        self.obj.image = tempfile.NamedTemporaryFile(suffix='.jpg').name
        self.obj.save()

    def test_str_method(self):
        self.assertIsNotNone(self.obj)
        self.assertEqual(str(self.obj), 'project fake')

    def test_auto_generate_image_alt(self):
        self.assertTrue(self.obj.image_alt)
        self.assertEquals(self.obj.image_alt, 'gallery-fake')

    def test_fields_model(self):
        self.assertTrue(self.obj.image)
        self.assertEquals(self.obj.title, 'gallery fake')
        self.assertEquals(self.obj.project, self.project)
