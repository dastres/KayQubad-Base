import base64
import json
import tempfile

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from marketing.models import UserComment
from marketing.api.serializer import (
    UserCommentSerializer
)


class UserCommentViewSetTestCase(APITestCase):
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

        self.user_comment = UserComment.objects.create(
            name='admin',
            company='web',
            content='content test',
            rate=4,
        )

        self.valid_data = {
            'name': 'name valid',
            'company': 'company valid',
            'content': 'content valid',
            'rate': 5,
        }

        self.no_valid_data = {
            'name': 'name valid',
            'company': 'company valid',
            'content': 'content valid',
            'rate': 10,
        }

    # ________________________ List ______________________________
    def test_user_comment_list(self):
        path = reverse('marketing:user_comment-list')
        response = self.client.get(path)

        user_comments = UserComment.objects.all().order_by('-created_at')
        serializer = UserCommentSerializer(user_comments, many=True)

        self.assertTrue(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], serializer.data)

    # ________________________ Create ______________________________
    def test_useer_comment_create_valid_data(self):
        path = reverse('marketing:user_comment-list')
        response = self.client.post(path, self.valid_data, **self.auth_headers)

        serializer = UserCommentSerializer(data=self.valid_data)
        serializer.is_valid(raise_exception=True)
        content = json.loads(response.content)

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(content.get('name'), self.valid_data.get('name'))
        self.assertEquals(content.get('company'), self.valid_data.get('company'))
        self.assertEquals(content.get('content'), self.valid_data.get('content'))
        self.assertTrue(content.get('rate'))
        self.assertTrue(content.get('avatar_alt'))

    def test_user_comment_create_no_valid_data(self):
        path = reverse('marketing:user_comment-list')
        response = self.client.post(path, self.no_valid_data, **self.auth_headers)

        serializer = UserCommentSerializer(data=self.no_valid_data)
        serializer.is_valid(raise_exception=False)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotEqual(response.status_code, status.HTTP_201_CREATED)

    # ________________________ Delete ______________________________
    def test_user_comment_delete(self):
        path = reverse('marketing:user_comment-detail', kwargs={'pk': 1})
        response = self.client.delete(path, **self.auth_headers)

        user_comment = UserComment.objects.all().count()

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEquals(user_comment, 0)

    # ________________________ Update ______________________________
    # def test_user_comment_update_valid_data(self):
    #     path = reverse('marketing:user_comment-detail', kwargs={'pk': 1})
    #
    #     serializer = UserCommentSerializer(data=self.valid_data)
    #     serializer.is_valid(raise_exception=True)
    #
    #     response = self.client.put(path=path, data=serializer.data, **self.auth_headers)
    #     content = json.loads(response.content)
    #
    #     self.assertEquals(response.status_code, status.HTTP_200_OK)
    #     self.assertEquals(content.get('name'), self.valid_data.get('name'))
    #     self.assertEqual(content.get('company'), self.valid_data.get('company'))
    #     self.assertEqual(content.get('content'), self.valid_data.get('content'))
    #     self.assertIsNotNone(content.get('rate')) # TODO : bugfix

    def test_user_comment_update_no_valid_data(self):
        path = reverse('marketing:user_comment-detail', kwargs={'pk': 1})

        serializer = UserCommentSerializer(data=self.no_valid_data)
        serializer.is_valid(raise_exception=False)

        response = self.client.put(path=path, data=serializer.data, **self.auth_headers)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotEqual(response.status_code, status.HTTP_201_CREATED)


    # ------------------------------ Search ------------------------------------

    def test_contact_us_list_search_successes(self):
        path = reverse('marketing:user_comment-list') + "?search=web"
        response = self.client.get(path, **self.auth_headers)
        content = json.loads(response.content)

        self.assertEquals(len(content['results']), 1)

    def test_contact_us_list_search_no_successes(self):
        path = reverse('marketing:user_comment-list') + "?search=xoxoxoxo"
        response = self.client.get(path, **self.auth_headers)
        content = json.loads(response.content)

        self.assertNotEquals(len(content['results']), 1)
        self.assertEquals(len(content['results']), 0)

    # ------------------------------ Filtering ------------------------------------

    def test_post_list_filtering_successes(self):
        path = reverse('marketing:user_comment-list') + "?company=web"
        response = self.client.get(path, **self.auth_headers)
        content = json.loads(response.content)

        self.assertEquals(len(content['results']), 1)

    def test_post_list_filtering_no_successes(self):
        path = reverse('marketing:user_comment-list') + "?company=ssss"
        response = self.client.get(path, **self.auth_headers)
        content = json.loads(response.content)

        self.assertNotEquals(len(content['results']), 1)
        self.assertEquals(len(content['results']), 0)