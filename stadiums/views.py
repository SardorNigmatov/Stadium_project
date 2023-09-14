from rest_framework.response import Response
from .models import StadiumsModels, BronModel
from .serializers import BronSerializers, StadiumsSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView, \
    RetrieveAPIView, DestroyAPIView, UpdateAPIView
from .permissions import StadionPermission




class AllStadiumsView(ListAPIView):
    queryset = StadiumsModels.objects.all()
    serializer_class = StadiumsSerializer

class DetailStadiumsView(RetrieveAPIView):
    queryset = StadiumsModels.objects.all()
    serializer_class = StadiumsSerializer


class CreateStadiumsView(CreateAPIView):
    permission_classes = (StadionPermission, IsAuthenticated)
    queryset = StadiumsModels.objects.all()
    serializer_class = StadiumsSerializer

class UpdateStadiumsView(UpdateAPIView):
    permission_classes = (StadionPermission, IsAuthenticated)
    queryset = StadiumsModels.objects.all()
    serializer_class = StadiumsSerializer

class DeleteStadiumsView(DestroyAPIView):
    permission_classes = (StadionPermission, IsAuthenticated)
    queryset = StadiumsModels.objects.all()
    serializer_class = StadiumsSerializer



class BronCreateApiew(CreateAPIView):
    queryset = BronModel.objects.all()
    serializer_class = BronSerializers
    permission_classes = (StadionPermission,IsAuthenticated)


class BronedListView(ListAPIView):
    queryset = BronModel.objects.all()
    serializer_class = BronSerializers

class BronedDeleteView(DestroyAPIView):
    queryset = BronModel.objects.all()
    serializer_class = BronSerializers
    permission_classes = (StadionPermission,IsAuthenticated)

class BronedUpdateView(UpdateAPIView):
    queryset = BronModel.objects.all()
    serializer_class = BronSerializers
    permission_classes = (StadionPermission,IsAuthenticated)
