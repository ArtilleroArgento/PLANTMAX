from django.urls import path
from . import views

urlpatterns = [
    path('', views.plant_list, name='plant_list'),
    path('search/', views.plant_search, name='plant_search'),
]