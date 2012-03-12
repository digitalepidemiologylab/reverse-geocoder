# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models

class Place(models.Model):
	#State fips code
	statefp10 = models.CharField(max_length=2)
	#Place fips code
	placefp10 = models.CharField(max_length=5)
	#Place ANSI code
	placens10 = models.CharField(max_length=8)
	#A concatenation of state fips code and place fips code
	geoid10 = models.CharField(max_length=7)
	#Census place name
	name10 = models.CharField(max_length=100)
	#Census place name and legal/statistical area description
	namelsad10 = models.CharField(max_length=100)
	#Legal/statistical area description code for place (city, town, etc)
	lsad10 = models.CharField(max_length=2)
	#Fips Class code
	classfp10 = models.CharField(max_length=2)
	#Principal city indicator
	pcicbsa10 = models.CharField(max_length=1)
	#New England city and town area principal city indicator
	pcinecta10 = models.CharField(max_length=1)
	#MAF/Tiger feature class code
	mtfcc10 = models.CharField(max_length=5)
	#Functional Status
	funcstat10 = models.CharField(max_length=1)
	#Land area
	aland10 = models.FloatField()
	#Water area
	awater10 = models.FloatField()
	#Latitude of internal point
	intptlat10 = models.CharField(max_length=11)
	#Longitude of internal point
	intptlon10 = models.CharField(max_length=12)
	geom = models.MultiPolygonField(srid=4326)
	objects = models.GeoManager()

	class Meta:
		app_label = 'geosera'

	def __unicode__(self):
		return self.name10


# Auto-generated `LayerMapping` dictionary for Place model
place_mapping = {
    'statefp10' : 'STATEFP10',
    'placefp10' : 'PLACEFP10',
    'placens10' : 'PLACENS10',
    'geoid10' : 'GEOID10',
    'name10' : 'NAME10',
    'namelsad10' : 'NAMELSAD10',
    'lsad10' : 'LSAD10',
    'classfp10' : 'CLASSFP10',
    'pcicbsa10' : 'PCICBSA10',
    'pcinecta10' : 'PCINECTA10',
    'mtfcc10' : 'MTFCC10',
    'funcstat10' : 'FUNCSTAT10',
    'aland10' : 'ALAND10',
    'awater10' : 'AWATER10',
    'intptlat10' : 'INTPTLAT10',
    'intptlon10' : 'INTPTLON10',
    'geom' : 'MULTIPOLYGON',
}
