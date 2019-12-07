from django.shortcuts import render

from sightings.models import Squirrel

def map(request, *args, **kwargs):
    sightings = Squirrel.objects.all()[:25]
    context = {
	'sigtings':sightings
    }
    return render(request, 'map/map.html',context)
