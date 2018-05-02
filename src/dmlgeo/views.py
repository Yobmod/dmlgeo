from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template.loader import render_to_string
from .models import Waypoint
# Create your views here.


def geo_index(request: HttpRequest) -> HttpResponse:
    return render(request, 'dmlgeo/geo_index.html')


def waypoints_index(request: HttpRequest) -> HttpResponse:
    'Display map'
    waypoints = Waypoint.objects.order_by('name')
    context = {
                'waypoints': waypoints,
                'content': render_to_string('waypoints/waypoints.html', {'waypoints': waypoints}),
    }
    return render(request, 'dmlgeo/waypoints_index.html', {})

