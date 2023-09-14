from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .models import CustomUser
from .serelaizers import CustomUserSerializer

class SignUpUserViews(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
