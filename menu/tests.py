import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from .models import Resturant, Menu
from datetime import datetime


User = get_user_model()


@pytest.mark.django_db
def test_valid_create_resturant(client):
    data = {
        "name": "Good Resturant",
        "description": "Really Very Good Resturant",
    }

    client = APIClient()
    url = reverse("menu:create-resturant")

    admin = User(
        email="test@gmail.com", password="test12345678",
        is_active=True, is_superuser=True
    )
    admin.is_admin = True
    admin.save()

    client.force_authenticate(user=admin)
    response = client.post(url, data=data)
    assert response.status_code == 201


@pytest.mark.django_db
def test_valid_upload_menu(client):
    resturant = Resturant(
        name="Good Resturant", description="Really Very Good Resturant"
    )
    resturant.save()

    data = {
        "first_course": "first_course",
        "main_course": "main_course",
        "dessert": "dessert",
        "drink": "drink",
        "day": 1,
        "resturant": resturant.pk
    }

    client = APIClient()
    url = reverse("menu:upload-menu")

    admin = User(
        email="test@gmail.com", password="test12345678",
        is_active=True, is_superuser=True
    )
    admin.is_admin = True
    admin.save()

    client.force_authenticate(user=admin)
    response = client.post(url, data=data)
    assert response.status_code == 201


@pytest.mark.django_db
def test_see_menu_for_today(client):

    resturant = Resturant(
        name="Good Resturant", description="Really Very Good Resturant"
    )
    resturant.save()
    menu = Menu(
        first_course="first_course",
        main_course="main_course",
        dessert="dessert",
        drink="drink",
        day=datetime.today().weekday(),
        resturant=resturant
    )
    menu.save()

    url = reverse("menu:see-menu-for-today", kwargs={"pk": resturant.pk})
    response = client.get(url)
    assert response.status_code == 200
