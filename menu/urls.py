from django.urls import path
from .views import (
    CreateResturantView, UploadMenuView, SeeMenuForToday, LeaveMenuReview,
    SeeMenuRating
)

app_name = 'menu'

urlpatterns = [
    path(
        'create-resturant/', CreateResturantView.as_view(),
        name="create-resturant"
    ),
    path('upload_menu/', UploadMenuView.as_view(), name='upload-menu'),
    path(
        'today_menu/<int:pk>/', SeeMenuForToday.as_view(),
        name='see-menu-for-today'
    ),
    path('leave_review/', LeaveMenuReview.as_view(), name='leave-review'),
    path(
        'see_menu_rating/<int:pk>/', SeeMenuRating.as_view(),
        name='see_menu_rating'
    ),
]
