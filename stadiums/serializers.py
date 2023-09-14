from rest_framework import serializers
from .models import StadiumsModels,BronModel
class StadiumsSerializer(serializers.ModelSerializer):

    class Meta:
        model = StadiumsModels
        fields = ('name','address','contact','img','stadium_about')


class BronSerializers(serializers.ModelSerializer):
    class Meta:
        model = BronModel
        fields = ('first_name','last_name','phone_number','begin_time','end_time','is_broned','date')

