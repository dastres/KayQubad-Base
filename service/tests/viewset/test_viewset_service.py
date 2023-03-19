import json
import base64

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

from service.models import Service
from service.api.serializer import (
    ServiceListSerializer, ServiceDetailSerializer, ServiceCreateUpdateSerializer
)


class ServiceViewSetTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create(
            username='user',
            is_staff=True,
        )
        self.user.set_password('user123123')
        self.user.save()

        self.auth_headers = {
            'HTTP_AUTHORIZATION': 'Basic ' + base64.b64encode('user:user123123'.encode()).decode()
        }

        self.service = Service.objects.create(
            title='title service',
            content='content service',
            author=self.user,
            short_description='short description service',
            position='Left',
        )

        self.valid_date = {
            'title': 'title valid',
            'author': self.user,
            'content': 'content valid',
            'short_description': 'short description valid',
            'position': 'Right',
        }

        self.no_valid_date = {
            'title': '',
            'author': '',
            'content': '',
            'short_description': self.user,
            'position': self.user,
        }

        self.update_valid_date = {
            'title': 'title valid update',
            'author': self.user,
            'content': 'content valid update',
            'short_description': 'short description valid update',
            'position': 'Left',
        }

        self.no_update_valid_date = {
            'title': '',
            'author': '',
            'content': '',
            'short_description': self.user,
            'position': self.user,
        }

    # ---------------------------- List ________________________________________
    def test_service_list(self):
        path = reverse('service:service-list')
        response = self.client.get(path)

        service = Service.objects.all().order_by('-created_at')
        serializer = ServiceListSerializer(service, many=True)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data['results'], serializer.data)

    # ---------------------------- Create ________________________________________
    def test_service_create_valid_data(self):
        path = reverse('service:service-list')
        response = self.client.post(path=path, data=self.valid_date, **self.auth_headers)
        content = json.loads(response.content)

        serializer = ServiceCreateUpdateSerializer(data=self.valid_date)
        serializer.is_valid(raise_exception=True)

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(content.get('title'), self.valid_date.get('title'))
        self.assertEquals(content.get('content'), self.valid_date.get('content'))
        self.assertEquals(content.get('short_description'), self.valid_date.get('short_description'))
        self.assertEquals(content.get('position'), self.valid_date.get('position'))
        self.assertTrue(content.get('status'))
        self.assertTrue(content.get('slug'))

    def test_service_create_no_valid_data(self):
        path = reverse('service:service-list')
        response = self.client.post(path=path, data=self.no_valid_date, **self.auth_headers)

        serializer = ServiceCreateUpdateSerializer(data=self.no_valid_date)
        serializer.is_valid(raise_exception=False)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_service_create_no_permission(self):
        path = reverse('project:project-list')
        response = self.client.post(path=path, data=self.valid_date)

        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # ---------------------------- Detail ________________________________________
    def test_service_detail(self):
        path = reverse('service:service-detail', kwargs={'slug': 'title-service'})
        response = self.client.get(path)

        service = Service.objects.get(slug=self.service.slug)
        serializer = ServiceDetailSerializer(service)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    # ---------------------------- Delete ________________________________________

    def test_service_delete(self):
        path = reverse('service:service-detail', kwargs={'slug': 'title-service'})
        response = self.client.delete(path, **self.auth_headers)

        service = Service.objects.all().count()

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEquals(service, 0)

    def test_service_delete_no_permission(self):
        path = reverse('service:service-detail', kwargs={'slug': 'title-service'})
        response = self.client.delete(path)

        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # ---------------------------- Update ________________________________________
    def test_project_update_valid_data(self):
        path = reverse('service:service-detail', kwargs={'slug': 'title-service'})
        response = self.client.put(path=path, data=self.update_valid_date, **self.auth_headers)
        content = json.loads(response.content)

        serializer = ServiceCreateUpdateSerializer(data=self.valid_date)
        serializer.is_valid(raise_exception=True)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(content.get('title'), self.update_valid_date.get('title'))
        self.assertEquals(content.get('content'), self.update_valid_date.get('content'))
        self.assertEquals(content.get('short_description'), self.update_valid_date.get('short_description'))
        self.assertEquals(content.get('position'), self.update_valid_date.get('position'))
        self.assertTrue(content.get('status'))
        self.assertTrue(content.get('slug'))

    def test_project_update_no_valid_data(self):
        path = reverse('service:service-detail', kwargs={'slug': 'title-service'})
        response = self.client.put(path=path, data=self.no_update_valid_date, **self.auth_headers)

        serializer = ServiceCreateUpdateSerializer(data=self.no_update_valid_date)
        serializer.is_valid(raise_exception=False)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_project_update_no_permission(self):
        path = reverse('service:service-detail', kwargs={'slug': 'title-service'})
        response = self.client.put(path=path, data=self.valid_date)

        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

   # ------------------------------ Search ------------------------------------

    def test_service_search_successes(self):
        path = reverse("service:service-list") + "?search=title+service"
        response = self.client.get(path, **self.auth_headers)
        content = json.loads(response.content)

        self.assertEquals(len(content['results']), 1)

    def test_category_list_search_no_successes(self):
        path = reverse("service:service-list") + "?search=xoxoxoxo"
        response = self.client.get(path, **self.auth_headers)
        content = json.loads(response.content)

        self.assertNotEquals(len(content['results']), 1)
        self.assertEquals(len(content['results']), 0)

        # ------------------------------ Filtering ------------------------------------

    def test_service_filtering_successes(self):
        path = reverse("service:service-list") + "?position=Left"
        response = self.client.get(path, **self.auth_headers)
        content = json.loads(response.content)

        self.assertEquals(len(content['results']), 1)

    def test_service_filtering_no_successes(self):
        path = reverse("service:service-list") + "?position=Right"
        response = self.client.get(path, **self.auth_headers)
        content = json.loads(response.content)

        self.assertNotEqual(len(content['results']), 1)
        self.assertEquals(len(content['results']), 0)

   # -------------------------------- Pagination --------------------------

    def test_pagination_successes(self):
        path = reverse("service:service-list")
        response = self.client.get(path, **self.auth_headers)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('next', response.data)
        self.assertIn('previous', response.data)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['count'], 1)

    def test_pagination_404(self):
        path = reverse("service:service-list")
        response = self.client.get(path + '?page=2', **self.auth_headers)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertNotIn('next', response.data)
        self.assertNotIn('previous', response.data)
