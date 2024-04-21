import pytest
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


pytestmark = [pytest.mark.django_db]


class LoginTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()

        password = make_password('1')

        self.user = get_user_model().objects.create(
            email='admin@admin.admin',
            password=password,
            is_active=True
        )

        data = {
            "email": self.user.email,
            "password": "1"
        }

        url = reverse('jwt-create')

        self.token = 'Bearer ' + self.client.post(
            url,
            data=data,
            format='json'
        ).data['access']

    def test_login(self):
        url = reverse('test-login')
        self.client.credentials(HTTP_AUTHORIZATION=self.token)
        response = self.client.get(url)
        assert response.status_code == 200
        assert response.data == 'Privet yopta'