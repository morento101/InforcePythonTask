import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_valid_create_employee(client):
    data = {
        "email": "test@gmail.com",
        "password1": "test12345678",
        "password2": "test12345678",
    }

    url = reverse("authentication:create-employee")
    response = client.post(url, data=data)
    assert response.status_code == 201


@pytest.mark.django_db
def test_invalid_create_employee(client):
    data = {
        "email": "test@gmail.com",
        "password1": "test12345678",
        "password2": "wrong_password",
    }

    url = reverse("authentication:create-employee")
    response = client.post(url, data=data)
    assert response.status_code == 400
