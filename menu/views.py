from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView, get_object_or_404
)
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .serializers import ResturantSerializer, MenuSerializer, ReviewSerializer
from datetime import datetime
from .models import Menu, Resturant
from django.db.models import Avg
from rest_framework.response import Response


class CreateResturantView(CreateAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = ResturantSerializer


class UploadMenuView(CreateAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = MenuSerializer


class SeeMenuForToday(RetrieveAPIView):
    queryset = Resturant.objects.all()
    serializer_class = MenuSerializer

    def get_object(self):
        resturant = super().get_object()
        return get_object_or_404(
            Menu, resturant=resturant, day=datetime.today().weekday()
        )


class LeaveMenuReview(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ReviewSerializer


class SeeMenuRating(RetrieveAPIView):
    queryset = Resturant.objects.all()
    serializer_class = MenuSerializer

    def get_object(self):
        resturant = super().get_object()
        return get_object_or_404(
            Menu, resturant=resturant, day=datetime.today().weekday()
        )

    def retrieve(self, request, pk):
        obj = self.get_object()
        average_rating = obj.review_set.aggregate(Avg('rating'))
        return Response(average_rating)
