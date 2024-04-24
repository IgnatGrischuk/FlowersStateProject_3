from django.urls import path
from flowers_state.views import (FlowersListView,
                                 FlowerView,
                                 FlowerFertilizerView,
                                 FlowerWateringView,
                                 FlowerAdviceView)


urlpatterns = [
    path('flowers/', FlowersListView.as_view(), name='flowers'),
    path('flowers/create-flower/', FlowerView.as_view(), name='flower-create'),
    path('flowers/fertilizer/', FlowerFertilizerView.as_view(),
         name='flower-fertilizer'),
    path('flowers/create-fertilizer/', FlowerFertilizerView.as_view(),
         name='fertilizer-create'),
    path('flowers/watering/', FlowerWateringView.as_view(),
         name='flower-watering'),
    path('flowers/create-watering/', FlowerWateringView.as_view(),
         name='watering-create'),
    path('flowers/advice/<int:flower_id>/', FlowerAdviceView.as_view(),
         name='advice'),
]