from rest_framework import serializers
from .models import Resturant, Menu, Review


class ResturantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resturant
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
