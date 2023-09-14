from django.urls import path
from .views import BronCreateApiew, AllStadiumsView, DetailStadiumsView, CreateStadiumsView, UpdateStadiumsView, DeleteStadiumsView, BronedListView
urlpatterns = [
    path('bron/create/',BronCreateApiew.as_view(),name='bron_created'),
    path('stadion/create/',CreateStadiumsView.as_view(),name='stadion-create'),
    path('stadion/all/',AllStadiumsView.as_view(),name='stdion_all'),
    path('stadion/detail/',DetailStadiumsView.as_view(),name='stadion_detial'),
    path('stadion/delete',DeleteStadiumsView.as_view(),name='stadion_delete'),
    path('stadion/update/',UpdateStadiumsView.as_view(),name='stadion_update'),
    path('isbron/all/',BronedListView.as_view(),name='isbron'),
]