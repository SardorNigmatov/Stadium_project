from rest_framework import serializers
from .models import StadiumsModels, BronModel

class StadiumsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StadiumsModels
        fields = ('name','address','contact','img','stadium_about')

class BronedListSerializer(serializers.ModelSerializer):
    model = BronModel
    model = StadiumsModels
    fileds = ('StadiumsModels.name','first_name','last_name','phone_number','date','begin_time','end_time')
