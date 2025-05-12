import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_user_api():
    client = APIClient()
    response = client.post('/api/users/', {'username': 'testuser', 'password': 'password123'}, format='json')
    assert response.status_code == 201

@pytest.mark.django_db
def test_api_key_api():
    client = APIClient()
    user = User.objects.create_user(username="apiuser", password="password123")
    client.force_authenticate(user=user)
    response = client.post('/api/apikeys/', {}, format='json')
    assert response.status_code == 201
