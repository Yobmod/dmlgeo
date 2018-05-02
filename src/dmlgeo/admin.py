from django.contrib.gis import admin
from .models import (WorldBorder,
                    Zipcode,
                    Elevation,
)


class ZipCodeAdmin(admin.ModelAdmin):
    list_display = ["__str__", "code", "poly"]
    # form = ZipCodeForm
    class Meta:
        model = Zipcode


class ElevationAdmin(admin.ModelAdmin):
    list_display = ["__str__", "name", "rast"]

    class Meta:
        model = Elevation


admin.site.register(WorldBorder, admin.GeoModelAdmin)
admin.site.register(Zipcode, ZipCodeAdmin)
admin.site.register(Elevation, ElevationAdmin)

