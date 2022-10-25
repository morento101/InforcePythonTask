from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView, get_object_or_404
)
# from rest_framework.permissions import IsAdminUser
from .serializers import ResturantSerializer, MenuSerializer
from datetime import datetime
from .models import Menu, Resturant


class CreateResturantView(CreateAPIView):
    # permission_classes = (IsAdminUser,)
    serializer_class = ResturantSerializer


class UploadMenuView(CreateAPIView):
    serializer_class = MenuSerializer


class SeeMenuForToday(RetrieveAPIView):
    queryset = Resturant.objects.all()
    serializer_class = MenuSerializer

    def get_object(self):
        resturant = super().get_object()
        return get_object_or_404(
            Menu, resturant=resturant, day=datetime.today().weekday()
        )
