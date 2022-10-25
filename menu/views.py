from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser
from .serializers import ResturantSerializer


class CreateResturantView(CreateAPIView):
    # permission_classes = (IsAdminUser,)
    serializer_class = ResturantSerializer
