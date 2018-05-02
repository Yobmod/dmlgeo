import os
from django.contrib.gis.gdal import DataSource

"""https://docs.djangoproject.com/en/2.0/ref/contrib/gis/tutorial/"""

def print_world_borders_data():
    """Get the data"""
    DMLGEO_PATH = os.path.abspath(os.path.dirname(__file__))
    world_shp = os.path.join(DMLGEO_PATH, 'geodata', 'TM_WORLD_BORDERS-0.3.shp')
    
    ds = DataSource(world_shp)
    print(ds)
    print('No. of layers: ', len(ds)) # shapefiles  only have one layer
    
    lyr = ds[0] # selects the first(only) layer
    print('Layer name: ', lyr)
    print('Layer type: ', lyr.geom_type) # WorldBorder model defined above uses a MultiPolygonField (that subclasses PolygonField)
    print('No. of shapes: ', len(lyr))
    
    srs = lyr.srs  # spatial reference system associated with layer
    # print(srs) # popular WGS84 srs data, uses (longitude, latitude) pairs in degrees
    print('Proj4 reprn of spatial ref stsyem:', srs.proj4) # proj.4 representation
    print('Layer fields:', lyr.fields)
    # [fld.__name__ for fld in lyr.field_types]  # OGR types of each field
    return lyr

def print_WBD_country_list(datashape_layer):
    """fields: ['FIPS', 'ISO2', 'ISO3', 'UN', 'NAME', 'AREA', 'POP2005', 'REGION', 'SUBREGION', 'LON', 'LAT']"""
    for feat in datashape_layer:
        geom = feat.geom
        #if feat.get('NAME') == 'United Kingdom':
            #print(feat)
        print(feat.get('NAME'), geom.num_points)  # prints list of features, ie. countries and geometries
        # print(geom.json)  # print each country geometry as JSON
        # print(geom.wkt)  # print each country geometry as WKT
    # eg_country = datashape_layer[206]; print(eg_country.get('NAME'))  # select countries via list slices and attributed via get('layer field')


if __name__ == '__main__':
    layer = print_world_borders_data()
    print_WBD_country_list(layer)