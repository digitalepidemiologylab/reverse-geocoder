import os
from django.contrib.gis.utils import LayerMapping
from geosera.models.county import CountyBoundary 
from geosera.models.county import countyboundary_mapping

county_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/tiger_county_2010/tl_2010_us_county10.shp'))

def run(verbose=True):
	lm = LayerMapping(CountyBoundary, county_shp, countyboundary_mapping, transform=True, encoding='latin-1')
	lm.save(strict=True, verbose=verbose)
