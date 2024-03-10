from django.urls import path
from . import views
from plants.views import index

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.plant_search, name='plant_search'),
    
]
