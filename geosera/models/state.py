# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models

class State(models.Model):
	#Region code: (1 Northeast, 2 Midwest, 3 South, 4 West, 9 PR and Island Areas)
	region10 = models.CharField(max_length=2)
	#Divison code: Middle Atlantic, East South Central etc. 
	division10 = models.CharField(max_length=2)
	#State FIPS code
	statefp10 = models.CharField(max_length=2)
	#State ANSI code
	statens10 = models.CharField(max_length=8)
	#State FIPS code
	geoid10 = models.CharField(max_length=2)
	#Postal Service state abbreviation
	stusps10 = models.CharField(max_length=2)
	#State name
	name10 = models.CharField(max_length=100)
	#Area description code for state
	lsad10 = models.CharField(max_length=2)
	#MAF/Tiger feature class code
	mtfcc10 = models.CharField(max_length=5)
	#Functional status
	funcstat10 = models.CharField(max_length=1)
	#Land area (square meters)
	aland10 = models.FloatField()
	#Water area (square meters)
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
		return self.name10

# Auto-generated `LayerMapping` dictionary for State model
state_mapping = {
    'region10' : 'REGION10',
    'division10' : 'DIVISION10',
    'statefp10' : 'STATEFP10',
    'statens10' : 'STATENS10',
    'geoid10' : 'GEOID10',
    'stusps10' : 'STUSPS10',
    'name10' : 'NAME10',
    'lsad10' : 'LSAD10',
    'mtfcc10' : 'MTFCC10',
    'funcstat10' : 'FUNCSTAT10',
    'aland10' : 'ALAND10',
    'awater10' : 'AWATER10',
    'intptlat10' : 'INTPTLAT10',
    'intptlon10' : 'INTPTLON10',
    'geom' : 'MULTIPOLYGON',
}
