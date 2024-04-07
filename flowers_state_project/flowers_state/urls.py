from django.urls import path
from flowers_state.views import FlowersListView


urlpatterns = [
    path('flowers/', FlowersListView.as_view(), name='flowers'),
]