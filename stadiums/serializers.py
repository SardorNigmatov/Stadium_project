from rest_framework.serializers import ModelSerializer
from .models import StadiumsModels, BronModel
from django.shortcuts import get_object_or_404
from account.models import CustomUser


class StadiumsSerializer(ModelSerializer):
    class Meta:
        model = StadiumsModels
        fields = ('name','address','contact','img','stadium_about')
        
        
        def create(self, validated_data):
            print(self.context['request'].user.id)
            validated_data['user'] = get_object_or_404(CustomUser, id=self.context['request'].user.id)
            return super(StadiumsSerializer,self).create(validated_data)
        
        
        

# class BrondDelSerilaizer(serializers.ModelSerializer):
#     class Meta:
#         model = BronModel
#         fields = ('stadion_id','first_name','last_name','phone_number','date','begin_time','end_time','is_broned')
        
#     def delete(self, validat_data):
        