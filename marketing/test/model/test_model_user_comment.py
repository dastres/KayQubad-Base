import tempfile

from django.test import TestCase
from marketing.models import UserComment


class UserCommentModelTestCase(TestCase):
    def setUp(self) -> None:
        self.user_comment = UserComment.objects.create(
            name='admin',
            company='web',
            avatar=tempfile.NamedTemporaryFile(suffix='.jpg').name,
            content='content test',
            rate=4,
        )

    def test_method_str(self):
        self.assertTrue(self.user_comment)
        self.assertEquals(str(self.user_comment), 'admin')
        self.assertNotEquals(str(self.user_comment), 'sub category fake')

    def test_auto_generate_avatar_alt(self):
        self.assertTrue(self.user_comment.avatar_alt)
        self.assertEquals(self.user_comment.avatar_alt, 'admin')

    def test_fields_model_user_comment(self):
        self.assertTrue(self.user_comment.created_at)
        self.assertEquals(self.user_comment.company, 'web')
        self.assertEquals(self.user_comment.rate, 4)
        self.assertEquals(self.user_comment.content, 'content test')
        self.assertIsNotNone(self.user_comment.is_active)
