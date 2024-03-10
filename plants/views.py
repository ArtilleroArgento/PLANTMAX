from django.shortcuts import render
from .models import Plant


def index(request):
    plants = Plant.objects.all()
    return render(request, 'plants/index.html', {'plants': plants})

def plant_search(request):
    query = request.GET.get('q')
    plants = Plant.objects.filter(name__icontains=query)
    return render(request, 'plants/plant_list.html', {'plants': plants})

