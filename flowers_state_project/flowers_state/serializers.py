from rest_framework import serializers
from .models import Flower, CustomUser


class CustomUserSerializer(serializers.Serializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email')


class FlowerSerializer(serializers.Serializer):
    user = CustomUserSerializer()

    class Meta:
        model = Flower
        fields = ('id', 'name', 'description', 'user')
