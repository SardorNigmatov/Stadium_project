from rest_framework import serializers
from .models import StadiumsModels
from account.models import CustomUser
class StadiumsSerializer(serializers.ModelSerializer):




    class Meta:
        model = StadiumsModels
        fields = ('name','address','contact','img','stadium_about')
