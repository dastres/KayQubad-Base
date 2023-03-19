import base64
import json

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from marketing.models import EmailSubscription
from marketing.api.serializer import (
    EmailSubscriptionCreateUpdateSerializer, EmailSubscriptionListDetailSerializer
)


class EmailSubscriptionViewSetTestCase(APITestCase):
    def setUp(self) -> None:
        self.author = get_user_model().objects.create(
            username='author',
            is_staff=True
        )
        self.author.set_password('author123123')
        self.author.save()

        self.auth_headers = {
            'HTTP_AUTHORIZATION': 'Basic ' + base64.b64encode('author:author123123'.encode()).decode()
        }

        self.email_sub = EmailSubscription.objects.create(
            email='admin@gmail.com'
        )

        self.valid_data = {
            'email': 'admin2@gmail.com'
        }

        self.no_valid_data = {
            'email': 'dssfsdfsd'
        }

    # ________________________ List ______________________________
    def test_email_subscription_list(self):
        path = reverse('marketing:email_subscription-list')
        response = self.client.get(path)

        email_subscription = EmailSubscription.objects.all().order_by('-created_at')
        serializer = EmailSubscriptionListDetailSerializer(email_subscription, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], serializer.data)

    # ________________________ Create ______________________________
    def test_email_subscription_create_valid_data(self):
        path = reverse('marketing:email_subscription-list')
        response = self.client.post(path, self.valid_data, **self.auth_headers)

        serializer = EmailSubscriptionCreateUpdateSerializer(data=self.valid_data)
        serializer.is_valid(raise_exception=True)
        content = json.loads(response.content)

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(content.get('email'), self.valid_data.get('email'))

    def test_email_subscription_create_no_valid_data(self):
        path = reverse('marketing:email_subscription-list')
        response = self.client.post(path, self.no_valid_data, **self.auth_headers)

        serializer = EmailSubscriptionCreateUpdateSerializer(data=self.no_valid_data)
        serializer.is_valid(raise_exception=False)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotEqual(response.status_code, status.HTTP_201_CREATED)

    # ________________________ Delete ______________________________
    def test_user_comment_delete(self):
        path = reverse('marketing:email_subscription-detail', kwargs={'pk': 1})
        response = self.client.delete(path, **self.auth_headers)

        email_subscription = EmailSubscription.objects.all().count()

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEquals(email_subscription, 0)

    # ________________________ Update ______________________________
    def test_email_subscription_update_valid_data(self):
        path = reverse('marketing:email_subscription-detail', kwargs={'pk': 1})

        serializer = EmailSubscriptionCreateUpdateSerializer(data=self.valid_data)
        serializer.is_valid(raise_exception=True)

        response = self.client.put(path=path, data=serializer.data, **self.auth_headers)
        content = json.loads(response.content)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(content.get('email'), self.valid_data.get('email'))

    def test_email_subscription_update_no_valid_data(self):
        path = reverse('marketing:email_subscription-detail', kwargs={'pk': 1})

        serializer = EmailSubscriptionCreateUpdateSerializer(data=self.no_valid_data)
        serializer.is_valid(raise_exception=False)

        response = self.client.put(path=path, data=serializer.data, **self.auth_headers)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotEqual(response.status_code, status.HTTP_201_CREATED)

        # ------------------------------ Search ------------------------------------

    def test_contact_us_list_search_successes(self):
        path = reverse('marketing:email_subscription-list') + "?search=admin@gmail.com"
        response = self.client.get(path, **self.auth_headers)
        content = json.loads(response.content)

        self.assertEquals(len(content['results']), 1)

    def test_contact_us_list_search_no_successes(self):
        path = reverse('marketing:email_subscription-list') + "?search=xoxoxoxo"
        response = self.client.get(path, **self.auth_headers)
        content = json.loads(response.content)

        self.assertNotEquals(len(content['results']), 1)
        self.assertEquals(len(content['results']), 0)

        # ------------------------------ Filtering ------------------------------------

    def test_post_list_filtering_successes(self):
        path = reverse('marketing:email_subscription-list') + "?email=admin@gmail.com"
        response = self.client.get(path, **self.auth_headers)
        content = json.loads(response.content)

        self.assertEquals(len(content['results']), 1)

    def test_post_list_filtering_no_successes(self):
        path = reverse('marketing:email_subscription-list') + "?email=nima@gmail.com"
        response = self.client.get(path, **self.auth_headers)
        content = json.loads(response.content)

        self.assertNotEquals(len(content['results']), 1)
        self.assertEquals(len(content['results']), 0)
