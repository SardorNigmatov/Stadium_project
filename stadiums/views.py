from django.shortcuts import render
from .models import BronModel
from rest_framework.generics import CreateAPIView
from .serializers import BronSerializers

# Create your views here.

class BronCreateApiew(CreateAPIView):
    queryset = BronModel.objects.all()
    serializer_class = BronSerializers