from django.contrib import admin
from .models import (Flower, FlowerImage, FlowerAdvice, FlowerWatering,
                     FlowerFertilizer)


class ProductAdmin(admin.ModelAdmin):
    list_display = ()
    search_fields = ()


admin.site.register(Flower, ProductAdmin)
admin.site.register(FlowerAdvice)
admin.site.register(FlowerFertilizer)
admin.site.register(FlowerWatering)
admin.site.register(FlowerImage)
