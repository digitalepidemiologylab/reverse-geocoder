import os
from django.contrib.gis.utils import LayerMapping
from geosera.models.zipcode import ZipCode 
from geosera.models.zipcode import zipcode_mapping

def run(verbose=True):
	shp_file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/tiger_zcta_2010/tl_2010_us_zcta510.shp'))
	lm = LayerMapping(ZipCode, shp_file, zipcode_mapping, transform=True, encoding='latin-1')
	lm.save(strict=True, verbose=verbose)
