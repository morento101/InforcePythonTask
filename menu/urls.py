from django.urls import path
from .views import CreateResturantView, UploadMenuView, SeeMenuForToday

urlpatterns = [
    path(
        'resturants/', CreateResturantView.as_view(), name="create-resturant"
    ),
    path('upload_menu/', UploadMenuView.as_view(), name='upload-menu'),
    path(
        'today_menu/<int:pk>/', SeeMenuForToday.as_view(),
        name='see-menu-for-today'
    )
]
