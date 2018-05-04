from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template.loader import render_to_string
from .models import Waypoint
# Create your views here.
from django.conf import settings

def geo_index(request: HttpRequest) -> HttpResponse:
    return render(request, 'dmlgeo/geo_index.html')


def waypoints_index(request: HttpRequest) -> HttpResponse:
    'Display map'
    google_map_api_key = settings.GOOGLE_MAP_API_KEY ; print(google_map_api_key)
    waypoints = Waypoint.objects.order_by('name')
    context = {
                'google_map_api_key': google_map_api_key,
                'waypoints': waypoints,
                #'content': render_to_string('dmlgeo/waypoints.html', {'waypoints': waypoints}),
    }
    return render(request, 'dmlgeo/waypoints_index.html', context)
