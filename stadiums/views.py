from rest_framework.response import Response
from .models import StadiumsModels, BronModel
from .serializers import BronSerializers, StadiumsSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView, \
    RetrieveAPIView, DestroyAPIView, UpdateAPIView
from permissions import AdminPermission, StadionPermission




class AllStadiumsView(ListAPIView):
    queryset = StadiumsModels.objects.all()
    serializer_class = StadiumsSerializer

class DetailStadiumsView(RetrieveAPIView):
    queryset = StadiumsModels.objects.all()
    serializer_class = StadiumsSerializer
    permission_classes = (StadionPermission,IsAuthenticated)

class CreateStadiumsView(CreateAPIView):
    queryset = StadiumsModels.objects.all()
    serializer_class = StadiumsSerializer
    permission_classes = (StadionPermission,IsAuthenticated)

class UpdateStadiumsView(UpdateAPIView):
    queryset = StadiumsModels.objects.all()
    serializer_class = StadiumsSerializer
    permission_classes = (StadionPermission,IsAuthenticated)

class DeleteStadiumsView(DestroyAPIView):
    queryset = StadiumsModels.objects.all()
    serializer_class = StadiumsSerializer
    permission_classes = (StadionPermission,IsAuthenticated)



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
