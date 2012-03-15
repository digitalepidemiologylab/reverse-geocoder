# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models

class ZipCode(models.Model):
	""" This actually stores a Zip Code Tabulation Area as defined by the US
	Census Bureau. Note that this is not entirely the same as the Zip Codes
	that the USPS uses. """

	#5-digit zip code tabluation area
	zcta5ce10 = models.CharField(max_length=5)
	#5-digit zip code tabulation area code
	geoid10 = models.CharField(max_length=5)
	#FIPS class code (55)
	classfp10 = models.CharField(max_length=2)
	#MAF/TIGER feature class code
	mtfcc10 = models.CharField(max_length=5)
	#Functional status
	funcstat10 = models.CharField(max_length=1)
	#Land area in square meters
	aland10 = models.FloatField()
	#Water area in square meters
	awater10 = models.FloatField()
	#Latitude of the internal point
	intptlat10 = models.CharField(max_length=11)
	#Longitude of the internal point
	intptlon10 = models.CharField(max_length=12)
	geom = models.MultiPolygonField(srid=4326)
	objects = models.GeoManager()

	class Meta:
		app_label = 'geosera'

	def __unicode__(self):
		return self.zcta5ce10

# Auto-generated `LayerMapping` dictionary for ZipCode model
zipcode_mapping = {
    'zcta5ce10' : 'ZCTA5CE10',
    'geoid10' : 'GEOID10',
    'classfp10' : 'CLASSFP10',
    'mtfcc10' : 'MTFCC10',
    'funcstat10' : 'FUNCSTAT10',
    'aland10' : 'ALAND10',
    'awater10' : 'AWATER10',
    'intptlat10' : 'INTPTLAT10',
    'intptlon10' : 'INTPTLON10',
    'geom' : 'MULTIPOLYGON',
}
