from django.urls import path
from .views import CreateEmployeeView

app_name = 'authentication'

urlpatterns = [
    path('employees/', CreateEmployeeView.as_view(), name="create-employee"),
]
