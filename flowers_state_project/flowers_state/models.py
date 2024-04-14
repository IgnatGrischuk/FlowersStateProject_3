from django.db import models
from users.models import CustomUser


class Flower(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class FlowerImage(models.Model):
    flowers = models.ForeignKey(Flower, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='flower_image/')

    def __str__(self):
        return f"Image {self.flowers}"


class FlowerWatering(models.Model):
    watering_time = models.ForeignKey(Flower, on_delete=models.CASCADE)

    def __str__(self):
        return (f"flowers: {self.watering_time}"
                f"time: {self.watering_time}\n")


class FlowerFertilizer(models.Model):
    fertilizer_time = models.ForeignKey(Flower, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.fertilizer_time}"


class FlowerAdvice(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.description[:50]}"
