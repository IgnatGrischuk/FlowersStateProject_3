from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import F

from flowers_state.models import (Flower, FlowerFertilizer,
                                  FlowerWatering, FlowerAdvice)
from flowers_state.serializers import (FlowerSerializer,
                                       FlowerFertilizerSerializer,
                                       FlowerWateringSerializer,
                                       FlowerAdviceSerializer)
from flowers_state.tasks import some_task
from drf_yasg.utils import swagger_auto_schema


class FlowersListView(APIView):
    permission_classes = (AllowAny, )

    @swagger_auto_schema(
        request_method="Get",
        responses={
            "200": "FlowerSerializer",
        }
    )
    def get(self, request):
        queryset = Flower.objects.all()
        print(some_task.delay().get())
        serializer = FlowerSerializer(queryset, many=True)
        return Response(serializer.data)


class FlowerView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        input_serializer = FlowerSerializer(data=request.data,)
        input_serializer.is_valid(raise_exception=True)
        user = request.user
        input_serializer.save(user=user)

        return Response()


class FlowerFertilizerView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        queryset = FlowerFertilizer.objects.all()
        serializer = FlowerFertilizerSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        input_serializer = FlowerFertilizerSerializer(data=request.data,)
        input_serializer.is_valid(raise_exception=True)
        user = request.user
        input_serializer.save(user=user)

        return Response()


class FlowerWateringView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        queryset = FlowerWatering.objects.all()
        serializer = FlowerWateringSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        input_serializer = FlowerWateringSerializer(data=request.data,)
        input_serializer.is_valid(raise_exception=True)
        user = request.user
        input_serializer.save(user=user)

        return Response()


class FlowerAdviceView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, flower_id):
        queryset = FlowerAdvice.objects.all().filter(flowers=flower_id)
        serializer = FlowerAdviceSerializer(queryset, many=True)
        return Response(serializer.data)
