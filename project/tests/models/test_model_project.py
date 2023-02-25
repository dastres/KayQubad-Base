from django.contrib.auth import get_user_model
from django.test import TestCase
from project.models import Project, ProjectCategory


class ProjectModelTestCase(TestCase):
    def setUp(self) -> None:
        self.category = ProjectCategory.objects.create(
            title='sub category fake',
            description='sub description fake',
        )

        self.author = get_user_model().objects.create(
            username='author',
            password='author123'
        )

        self.obj = Project.objects.create(
            title='project fake',
            content='content fake',
            author=self.author,
            category=self.category,
        )

    def test_method_str(self):
        self.assertEquals(str(self.obj), 'project fake')
        self.assertNotEquals(str(self.obj), 'sub category fake')

    def test_auto_generate_slug(self):
        self.assertTrue(self.obj.slug)
        self.assertEquals(self.obj.slug, 'project-fake')
        self.assertNotEquals(self.obj.slug, 'sub-category-fake')

    def test_auto_generate_thumbnail_alt(self):
        self.assertTrue(self.obj.thumbnail_alt)
        self.assertEquals(self.obj.thumbnail_alt, 'project-fake')
        self.assertNotEquals(self.obj.thumbnail_alt, 'sub-category-fake')

    def test_fields_model_category(self):
        self.assertTrue(self.obj.created_at)
        self.assertEquals(self.obj.content, 'content fake')
        self.assertIsNotNone(self.obj.status)
        self.assertIsNotNone(self.obj.is_active)
