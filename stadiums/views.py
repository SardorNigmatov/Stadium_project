from django.shortcuts import render
from .models import StadiumsModels
from .serializers import StadiumsSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView, \
    RetrieveAPIView, DestroyAPIView, UpdateAPIView

class AllStadiumsView(ListAPIView):
    queryset = StadiumsModels.objects.all()
    serializer_class = StadiumsSerializer

class DetailStadiumsView(RetrieveAPIView):
    queryset = StadiumsModels.objects.all()
    serializer_class = StadiumsSerializer

class CreateStadiumsView(CreateAPIView):
    queryset = StadiumsModels.objects.all()
    serializer_class = StadiumsSerializer
    # permission_classes = (IsAuthenticated,)

class UpdateStadiumsView(UpdateAPIView):
    queryset = StadiumsModels.objects.all()
    serializer_class = StadiumsSerializer
    # permission_classes = (IsAuthenticated,)

class DeleteStadiumsView(DestroyAPIView):
    queryset = StadiumsModels.objects.all()
    serializer_class = StadiumsSerializer
    # permission_classes = (IsAuthenticated,)


from .models import BronModel
from rest_framework.generics import CreateAPIView
from .serializers import BronSerializers


# Create your views here.

class BronCreateApiew(CreateAPIView):
    queryset = BronModel.objects.all()
    serializer_class = BronSerializers