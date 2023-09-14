from rest_framework import serializers
from .models import StadiumsModels
class StadiumsSerializer(serializers.ModelSerializer):




    class Meta:
        model = StadiumsModels
        fields = ('name','address','contact','img','stadium_about')
