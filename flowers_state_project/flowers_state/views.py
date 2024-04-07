from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .serializers import FlowerSerializer

from flowers_state.models import Flower


class FlowersListView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request):
        queryset = Flower.objects.all
        serializer = FlowerSerializer(queryset, many=True)
        return Response(serializer.data)