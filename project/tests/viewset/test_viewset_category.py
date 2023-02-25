import base64
import json

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from project.models import ProjectCategory
from project.api.serializer import (
    CategoryCreateUpdateSerializer, CategoryDetailSerializer, ListCategorySerializer
)


class CategoryViewSetTestCase(APITestCase):
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

        self.sub_category = ProjectCategory.objects.create(
            title='sub category fake',
            description='sub description fake',
        )

        self.category = ProjectCategory.objects.create(
            title='category fake',
            description='description fake',
            sub_category=self.sub_category
        )

        self.valid_date = {
            'title': 'title valid',
            'description': 'description valid',
            'categories': [self.category.id]
        }

        self.no_valid_date = {
            'title': '',
            'description': '',
            'categories': [self.user.id]
        }

        self.update_valid_date = {
            'title': 'title update valid',
            'description': 'description update valid',
            'categories': [self.category.id]
        }

        self.no_update_valid_date = {
            'title': '',
            'description': '',
            'categories': [self.user.id]
        }

    # ---------------------------- List ________________________________________
    def test_category_list(self):
        path = reverse('project:project_category-list')
        response = self.client.get(path)

        categories = ProjectCategory.objects.all()
        serializer = ListCategorySerializer(categories, many=True)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data, serializer.data)

    # ---------------------------- Create________________________________________

    def test_category_create_valid_data(self):
        path = reverse('project:project_category-list')
        response = self.client.post(path=path, data=self.valid_date, **self.auth_headers)
        content = json.loads(response.content)

        serializer = CategoryCreateUpdateSerializer(data=self.valid_date)
        serializer.is_valid(raise_exception=True)

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(content.get('title'), self.valid_date.get('title'))
        self.assertEquals(content.get('sub_category'), self.valid_date.get('sub_category'))
        self.assertEquals(content.get('description'), self.valid_date.get('description'))
        self.assertTrue(content.get('status'))

    def test_category_create_no_valid_data(self):
        path = reverse('project:project_category-list')
        response = self.client.post(path=path, data=self.no_valid_date, **self.auth_headers)

        serializer = CategoryCreateUpdateSerializer(data=self.no_valid_date)
        serializer.is_valid(raise_exception=False)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_category_create_no_permission(self):
        path = reverse('project:project_category-list')
        response = self.client.post(path=path, data=self.valid_date)

        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # ---------------------------- Detail ________________________________________
    def test_category_detail(self):
        path = reverse('project:project_category-detail', kwargs={'pk': 1})
        response = self.client.get(path)

        category = ProjectCategory.objects.get(id=self.sub_category.id)
        serializer = CategoryDetailSerializer(category)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    # ---------------------------- Delete ________________________________________
    def test_category_delete(self):
        path = reverse('project:project_category-detail', kwargs={'pk': 1})
        response = self.client.delete(path, **self.auth_headers)

        category = ProjectCategory.objects.all().count()

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEquals(category, 0)

    def test_category_delete_no_permission(self):
        path = reverse('portfolio:portfolio_category-detail', kwargs={'pk': 1})
        response = self.client.delete(path)

        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # ---------------------------- Update ________________________________________
    def test_category_update_valid_data(self):
        path = reverse('project:project_category-detail', kwargs={'pk': 1})
        response = self.client.put(path=path, data=self.update_valid_date, **self.auth_headers)
        content = json.loads(response.content)

        serializer = CategoryCreateUpdateSerializer(data=self.valid_date)
        serializer.is_valid(raise_exception=True)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(content.get('title'), self.update_valid_date.get('title'))
        self.assertEquals(content.get('sub_category'), self.update_valid_date.get('sub_category'))
        self.assertEquals(content.get('description'), self.update_valid_date.get('description'))
        self.assertTrue(content.get('status'))

    def test_category_update_no_valid_data(self):
        path = reverse('project:project_category-detail', kwargs={'pk': 1})
        response = self.client.put(path=path, data=self.no_update_valid_date, **self.auth_headers)

        serializer = CategoryCreateUpdateSerializer(data=self.no_update_valid_date)
        serializer.is_valid(raise_exception=False)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_category_update_no_permission(self):
        path = reverse('project:project_category-detail', kwargs={'pk': 1})
        response = self.client.put(path=path, data=self.valid_date)

        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)
