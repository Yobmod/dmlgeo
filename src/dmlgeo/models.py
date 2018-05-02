"""https://docs.djangoproject.com/en/2.0/ref/contrib/gis/model-api/"""

from django.contrib.gis.db import models

class WorldBorder(models.Model):
    # Regular Django fields corresponding to the attributes in the world borders shapefile.
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2)
    iso2 = models.CharField('2 Digit ISO', max_length=2)
    iso3 = models.CharField('3 Digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()
    mpoly = models.MultiPolygonField()  # GeoDjango-specific: a geometry field (MultiPolygonField)

    # Returns the string representation of the model.
    def __str__(self):
        return self.name


from django.contrib.gis.db.models import PointField
from django.db.models.functions import Cast



class Zipcode(models.Model):
    code = models.CharField(max_length=5)
    poly = models.PolygonField()

    def __str__(self):
        return self.code


class Elevation(models.Model):
    name = models.CharField(max_length=100)
    rast = models.RasterField()

    def __str__(self):
        return self.rast

""" to convert zipcodes to ????
geography type provides native support for spatial features represented with geographic coordinates (e.g., WGS84 longitude/latitude)
Zipcode.objects.annotate(
    geom=Cast('geography_field', PointField())
).filter(geom__within=poly)
"""
