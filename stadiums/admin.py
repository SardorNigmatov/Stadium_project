from django.contrib import admin
from .models import StadiumsModels,BronModel
# Register your models here.
class StadiumAdmin(admin.ModelAdmin):
    list_display = ('name','address','contact','img','stadium_about','user')
    search_fields = ['name','address']

class BronAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','phone_number','begin_time','end_time','date')

admin.site.register(StadiumsModels,StadiumAdmin)
admin.site.register(BronModel,BronAdmin)
