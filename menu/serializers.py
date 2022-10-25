from rest_framework import serializers
from .models import Resturant, Menu


class ResturantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resturant
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
