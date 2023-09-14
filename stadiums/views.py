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


# Create your views here.
