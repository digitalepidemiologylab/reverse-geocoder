import os
from django.contrib.gis.utils import LayerMapping
from geosera.models.state import State
from geosera.models.state import state_mapping

def run(verbose=True):
	shp_file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/tiger_state_2010/tl_2010_us_state10.shp'))
	lm = LayerMapping(State, shp_file, state_mapping, transform=True, encoding='latin-1')
	lm.save(strict=True, verbose=verbose)
