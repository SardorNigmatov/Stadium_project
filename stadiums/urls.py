from django.urls import path
from .views import (BronCreateApiew,
                    AllStadiumsView,
                    DetailStadiumsView,
                    CreateStadiumsView,
                    UpdateStadiumsView,
                    DeleteStadiumsView,
                    BronedListView,
                    BronedDeleteView,
                    BronedUpdateView,)


urlpatterns = [
    path('bron/create/',BronCreateApiew.as_view(),name='bron_created'),
    path('bron/delete/<int:pk>/',BronedDeleteView.as_view(),name='bron-delte'),
    path('bron/all/',BronedListView.as_view(),name='bron-all'),
    path('bron/update/',BronedUpdateView.as_view(),name='bron-update'),
    path('stadion/create/',CreateStadiumsView.as_view(),name='stadion-create'),
    path('stadion/all/',AllStadiumsView.as_view(),name='stdion_all'),
    path('stadion/detail/<int:pk>/',DetailStadiumsView.as_view(),name='stadion_detial'),
    path('stadion/delete/<int:pk>/',DeleteStadiumsView.as_view(),name='stadion_delete'),
    path('stadion/update/<int:pk>/',UpdateStadiumsView.as_view(),name='stadion_update'),

]