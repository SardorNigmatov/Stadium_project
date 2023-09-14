from rest_framework.response import Response

from .models import StadiumsModels, BronModel
from .serializers import BronedListSerializer, BronSerializers, StadiumsSerializer
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



class BronCreateApiew(CreateAPIView):
    queryset = BronModel.objects.all()
    serializer_class = BronSerializers


class BronedListView(ListAPIView):
    queryset = BronModel.objects.all()
    serializer_class = BronedListSerializer

class BronedDeleteView(DestroyAPIView):
    queryset = BronModel.objects.all()
    serializer_class = BronedListSerializer
