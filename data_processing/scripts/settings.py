

GEO_DATA_SOURCE = '/opt/code/reverse-geocoder/data_processing/data/location-data/'

#This is where the location data files end up when they have been processed.
GEO_DATA_SINK = ''

#Geocoder flags. We keep track of how a tweet was geocoded. These are the
#various statuses that are applicable. 
GEOCODER_FLAGS = {
	#Geocoding has not been attempted for this tweet
	'GEOCODER_NOT_ATTEMPED':'N',

	#This tweet was reverse geocoded by Geosera
	'GEOSERA':'G',

	#Geosera failed to reverse geocode this tweet
	'GEOSERA_FAILED':'GF',

	#This tweet was reverse geocoded by Yahoo! Places
	'YAHOO':'Y',

	#Yahoo! Places failed to reverse geocode this tweet
	'GEOCODER_YAHOO_FAILED':'YF'
}

DATABASES = {
	'default':{
		'HOST':'',
		'USER':'',
		'PASSWORD':'',
		'NAME':''
	}
}

COUNTY_POP_FILE = '/opt/code/reverse-geocoder/data_processing/data/CenPop2010_Mean_CO.txt'

try:
	from local_settings import *
except ImportError:
	pass
