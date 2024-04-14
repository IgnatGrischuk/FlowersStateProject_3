from rest_framework import serializers

from flowers_state.models import (Flower, FlowerFertilizer, FlowerWatering,
                                  FlowerImage, FlowerAdvice)
from users.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email',)
        read_only_fields = ('email',)


class FlowerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    user = UserSerializer()

    class Meta:
        model = Flower
        fields = ('id', 'name', 'description', 'user')

    def to_representation(self, instance):
        if ('request' in self.context and
                self.context['request'].method in ['POST']):
            return {'id': instance.id}
        else:
            return super().to_representation(instance)


class FlowerFertilizerSerializer(serializers.ModelSerializer):
    fertilizer_time = serializers.DateTimeField()
    flowers = FlowerSerializer()

    class Meta:
        model = FlowerFertilizer
        fields = ('id', 'fertilizer_time', 'flowers')

    def create(self, validated_data):
        flower = validated_data.pop('flowers')
        user = validated_data.pop('user')
        flower = Flower.objects.get(id=flower['id'])

        return FlowerFertilizer.objects.create(**validated_data,
                                               flowers=flower)


class FlowerWateringSerializer(serializers.ModelSerializer):
    watering_time = serializers.DateTimeField()
    flowers = FlowerSerializer()

    class Meta:
        model = FlowerWatering
        fields = ('id', 'watering_time', 'flowers')

    def create(self, validated_data):
        flower = validated_data.pop('flowers')
        user = validated_data.pop('user')
        flower = Flower.objects.get(id=flower['id'])

        return FlowerWatering.objects.create(**validated_data,
                                             flowers=flower)


class FlowerImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = FlowerImage
        fields = 'images'


class FlowerAdviceSerializer(serializers.ModelSerializer):
    flowers = FlowerSerializer()

    class Meta:
        model = FlowerAdvice
        fields = ('description', 'flowers')
