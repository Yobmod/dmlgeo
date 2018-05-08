from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template.loader import render_to_string # deprec? JSONResponse
import json # deprec?
from .models import Waypoint
# Create your views here.
from django.conf import settings

def geo_index(request: HttpRequest) -> HttpResponse:
    return render(request, 'dmlgeo/geo_index.html')

"""
Waypoint(name='New York', geometry='POINT(-73.9869510 40.7560540)').save()
Waypoint(name='Buenos Aires', geometry='POINT(-58.4173090 -34.6117810)').save()
Waypoint(name='Moscow', geometry='POINT(37.6176330 55.7557860)').save()
Waypoint(name='Atlanta', geometry='POINT(-84.3896630 33.7544870)').save()"""

def waypoints_index(request: HttpRequest) -> HttpResponse:
    'Display map'
    google_map_api_key = settings.GOOGLE_MAP_API_KEY  # ; print(google_map_api_key)
    waypoints = Waypoint.objects.order_by('name')  # .distinct('name')
    context = {
                'google_map_api_key': google_map_api_key,
                'waypoints': waypoints,
                'content': render_to_string('dmlgeo/waypoints.html', {'waypoints': waypoints}),
    }
    return render(request, 'dmlgeo/waypoints_index.html', context)


#from django.views.decorators.csrf import csrf_exempt
#from django.template.context_processors import csrf


#@csrf_exempt
def waypoints_save(request):
    'Save waypoints'
    context = {}
    #context.update(csrf(request))
    for waypointString in request.POST.get('waypointsPayload', '').splitlines():
        waypointID, waypointX, waypointY = waypointString.split()
        waypoint = Waypoint.objects.get(id=int(waypointID))
        waypoint.geometry.x = (float(waypointX))
        waypoint.geometry.y = (float(waypointY))
        waypoint.save()
        print(waypoint.geometry)
    return HttpResponse(json.dumps({'isOk':1}), context)
