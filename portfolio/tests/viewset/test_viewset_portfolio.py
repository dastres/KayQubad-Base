import json
import base64

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

from portfolio.models import PortfolioCategory, Portfolio
from portfolio.api.serializer import (
    PortfolioListSerializer, PortfolioDetailSerializer, PortfolioCreateUpdateSerializer
)


class PortfolioViewSetTestCase(APITestCase):
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

        self.category = PortfolioCategory.objects.create(
            title='category fake',
            description='description fake',
        )

        self.obj = Portfolio.objects.create(
            title='portfolio fake',
            content='content fake',
            author=self.user,
            category=self.category,
        )

        self.valid_date = {
            'title': 'title valid',
            'content': 'description valid',
            'category': self.category.id
        }

        self.no_valid_date = {
            'title': '',
            'content': '',
            'category': self.category.id
        }

        self.update_valid_date = {
            'title': 'title  update valid',
            'content': 'description  update valid',
            'category': self.category.id
        }

        self.no_update_valid_date = {
            'title': 'title valid',
            'content': '',
            'category': self.category.id
        }

    # ---------------------------- List ________________________________________
    def test_portfolio_list(self):
        path = reverse('portfolio:portfolio-list')
        response = self.client.get(path)

        portfolio = Portfolio.objects.all()
        serializer = PortfolioListSerializer(portfolio, many=True)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data, serializer.data)

    # ---------------------------- Create ________________________________________
    def test_portfolio_create_valid_data(self):
        path = reverse('portfolio:portfolio-list')
        response = self.client.post(path=path, data=self.valid_date, **self.auth_headers)
        content = json.loads(response.content)

        serializer = PortfolioCreateUpdateSerializer(data=self.valid_date)
        serializer.is_valid(raise_exception=True)

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(content.get('title'), self.valid_date.get('title'))
        self.assertEquals(content.get('category'), self.valid_date.get('category'))
        self.assertEquals(content.get('content'), self.valid_date.get('content'))
        self.assertTrue(content.get('status'))

    def test_portfolio_create_no_valid_data(self):
        path = reverse('portfolio:portfolio-list')
        response = self.client.post(path=path, data=self.no_valid_date, **self.auth_headers)

        serializer = PortfolioCreateUpdateSerializer(data=self.no_valid_date)
        serializer.is_valid(raise_exception=False)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_portfolio_create_no_permission(self):
        path = reverse('portfolio:portfolio-list')
        response = self.client.post(path=path, data=self.valid_date)

        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # ---------------------------- Detail ________________________________________
    def test_portfolio_detail(self):
        path = reverse('portfolio:portfolio-detail', kwargs={'pk': 1})
        response = self.client.get(path)

        portfolio = Portfolio.objects.get(id=self.obj.id)
        serializer = PortfolioDetailSerializer(portfolio)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    # ---------------------------- Delete ________________________________________

    def test_portfolio_delete(self):
        path = reverse('portfolio:portfolio-detail', kwargs={'pk': 1})
        response = self.client.delete(path, **self.auth_headers)

        portfolio = Portfolio.objects.all().count()

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEquals(portfolio, 0)

    def test_category_delete_no_permission(self):
        path = reverse('portfolio:portfolio-detail', kwargs={'pk': 1})
        response = self.client.delete(path)

        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # ---------------------------- Update ________________________________________
    def test_portfolio_update_valid_data(self):
        path = reverse('portfolio:portfolio-detail', kwargs={'pk': 1})
        response = self.client.put(path=path, data=self.update_valid_date, **self.auth_headers)
        content = json.loads(response.content)

        serializer = PortfolioCreateUpdateSerializer(data=self.valid_date)
        serializer.is_valid(raise_exception=True)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(content.get('title'), self.update_valid_date.get('title'))
        self.assertEquals(content.get('category'), self.update_valid_date.get('category'))
        self.assertEquals(content.get('content'), self.update_valid_date.get('content'))
        self.assertTrue(content.get('status'))

    def test_portfolio_update_no_valid_data(self):
        path = reverse('portfolio:portfolio-detail', kwargs={'pk': 1})
        response = self.client.put(path=path, data=self.no_update_valid_date, **self.auth_headers)

        serializer = PortfolioCreateUpdateSerializer(data=self.no_update_valid_date)
        serializer.is_valid(raise_exception=False)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_portfolio_update_no_permission(self):
        path = reverse('portfolio:portfolio-detail', kwargs={'pk': 1})
        response = self.client.put(path=path, data=self.valid_date)

        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)
