from django.urls import path
from .views import BronCreateApiew
urlpatterns = [
    path('bron/create/',BronCreateApiew.as_view(),name='bron_created'),
]