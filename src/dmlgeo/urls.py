
from django.urls import path

from . import views

app_name = 'dmlgeo'
urlpatterns = [
    path('', views.geo_index, name="geo_index"),

    path('waypoints', views.waypoints_index, name="waypoints_index"),
    path('waypoints/save', views.waypoints_save, name='waypoints_save'),
]
