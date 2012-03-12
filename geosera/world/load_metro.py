import os
from django.contrib.gis.utils import LayerMapping
from geosera.models.metro import MetropolitanStatisticalArea
from geosera.models.metro import metropolitanstatisticalarea_mapping

shp_file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/tiger_cbsa_2009/tl_2009_us_cbsa.shp'))

def run(verbose=True):
	lm = LayerMapping(MetropolitanStatisticalArea, shp_file,
		metropolitanstatisticalarea_mapping, transform=True, encoding='latin-1')
	lm.save(strict=True, verbose=verbose)
