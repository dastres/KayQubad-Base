import tempfile

from django.test import TestCase
from marketing.models import EmailSubscription


class EmailSubscriptionModelTestCase(TestCase):
    def setUp(self) -> None:
        self.email_subscription = EmailSubscription.objects.create(
            email='admin@gmail.com'
        )

    def test_method_str(self):
        self.assertTrue(self.email_subscription)
        self.assertEquals(str(self.email_subscription), 'admin@gmail.com')
        self.assertNotEquals(str(self.email_subscription), 'sub category fake')


    def test_fields_model_user_comment(self):
        self.assertTrue(self.email_subscription.created_at)
        self.assertTrue(self.email_subscription.updated_at)
        self.assertEquals(self.email_subscription.email, 'admin@gmail.com')

