from django.urls import path
from flowers_state.views import (FlowersListView, FlowerView,
                                 FlowerFertilizerView, FlowerWateringView,
                                 FlowerAdviceView)


urlpatterns = [
    path('flowers/', FlowersListView.as_view(), name='flowers'),
    path('flower/', FlowerView.as_view(), name='create'),
    path('flower-watering/', FlowerWateringView.as_view(),
         name='flower-watering'),
    path('flower-fertilizer/', FlowerFertilizerView.as_view(),
         name='flower-fertilizer'),
    path('flowers/advice/<int:flower_id>/', FlowerAdviceView.as_view(),
         name='advice'),
]
