from django.urls import path
from .views import CreateEmployeeView

urlpatterns = [
    path('employees/', CreateEmployeeView.as_view(), name="employees"),
]
