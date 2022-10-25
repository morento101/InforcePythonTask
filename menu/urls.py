from django.urls import path
from .views import CreateResturantView

urlpatterns = [
    path(
        'resturants/', CreateResturantView.as_view(), name="create-resturant"
    ),
]
