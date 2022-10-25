from rest_framework.generics import CreateAPIView
from .models import Employee
from .serializers import CreateEmployeeSerializer


class CreateEmployeeView(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = CreateEmployeeSerializer
