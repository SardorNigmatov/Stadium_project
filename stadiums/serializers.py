from rest_framework.serializers import ModelSerializer
from .models import StadiumsModels, BronModel
from django.shortcuts import get_object_or_404
from account.models import CustomUser


class StadiumsSerializer(ModelSerializer):
    class Meta:
        model = StadiumsModels
        fields = ('name','address','contact','img','stadium_about')
        
    def create(self, validated_data):
            validated_data['user'] = get_object_or_404(CustomUser, id=self.context['request'].user.id)
            return super(StadiumsSerializer,self).create(validated_data)


class BronSerializers(ModelSerializer):
    class Meta:
        model = BronModel
        fields = ('first_name','last_name','phone_number','begin_time','end_time','stadion_id','date','is_broned')
        
    # def create(self, validated_data):
    #     # print(self.context['request'])
    #     validated_data['stadion_id'] = get_object_or_404(StadiumsModels, user=self.context['request'].user)
    #     return super(BronSerializers,self).create(validated_data)