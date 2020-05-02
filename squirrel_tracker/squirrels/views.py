from django.shortcuts import render
from django.http import HttpResponse

from .models import Sighting 

def index(request):
    return HttpResponse("Hi This is a squirrels tracker app.")

def map(request):
    location = list()
    for i in Sighting.objects.all():
        location_dict = {}
        location_dict['latitude'] = i.latitude
        location_dict['longitude'] = i.longitude
        location.append(location_dict)
    return render(request, 'squirrels/map.html', {'location':location})

def list_sightings(request):
    squirrels = Sighting.objects.all()
    return render(reqeust, 'squirrels/sightings.html',{'squirrels': squirrels})

def get_sighting(request, squirrel_id):
    squirrel = Sighting.objects.get(unique_squirrel_id = squirrel_id)
    return render(request, 'squirrels/sighting.html', {'squirrel':squirrel})
 
