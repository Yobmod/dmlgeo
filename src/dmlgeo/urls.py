
from django.urls import path

from . import views

app_name = 'dmlgeo'
urlpatterns = [
    path('', views.geo_index, name="geo_index"),
]
