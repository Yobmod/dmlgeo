from django.shortcuts import render

# Create your views here.
def geo_index(request):
    return render(request, 'dmlgeo/geo_index.html')