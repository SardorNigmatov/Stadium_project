from django.shortcuts import render
from rest_framework.response import Response
from .models import BronModel, StadiumsModels
from rest_framework.generics import ListAPIView
from .serializers import BronedListSerializer
# Create your views here.

class BronedListView(ListAPIView):
    serializer_class = BronedListSerializer
    def get(self, request):
        queryset = BronModel.objects.filter(is_broned=True)
        if queryset.exists():
            data = self.serializer_class(queryset, many=True).data
            return Response(data)
        else:
            # Handle the case when there are no broned objects
            return Response("No broned objects found.")



