import os
from django.contrib.gis.utils import LayerMapping
from geosera.models.place import Place 
from geosera.models.place import place_mapping

place_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/tiger_place_2010/tl_2010_24_place10.shp'))

def run(verbose=True):
	lm = LayerMapping(Place, place_shp, place_mapping, transform=True, encoding='latin-1')
	lm.save(strict=True, verbose=verbose)
