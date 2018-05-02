import os
from django.contrib.gis.utils import LayerMapping
from .models import WorldBorder

"""Create map the world borders file datashape layer fields to the model"""
world_mapping = {
    'fips' : 'FIPS',
    'iso2' : 'ISO2',
    'iso3' : 'ISO3',
    'un' : 'UN',
    'name' : 'NAME',
    'area' : 'AREA',
    'pop2005' : 'POP2005',
    'region' : 'REGION',
    'subregion' : 'SUBREGION',
    'lon' : 'LON',
    'lat' : 'LAT',
    'mpoly' : 'MULTIPOLYGON',
}

"""Get the world borders datashape file. Relative path works as long as geodata folder in same dir"""
world_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'geodata', 'TM_WORLD_BORDERS-0.3.shp'),
)

def run(verbose: bool=True) -> None:
    """Apply map of world borders file datashape layer fields to the model"""
    lm = LayerMapping(
        WorldBorder, world_shp, world_mapping,
        transform=False,  # False because the data in the shapefile is already in WGS84 (SRID=4326).
        encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)