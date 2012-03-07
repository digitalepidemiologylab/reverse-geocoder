# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models

class CountyBoundary(models.Model):
	#2010 Census state FIPS codes
	statefp10 = models.CharField(max_length=2)

	#FIPS code
	countyfp10 = models.CharField(max_length=3)

	#ANSI code	
	countyns10 = models.CharField(max_length=8)
	#County identifier: a concatenation of 2010 Census state FIPS code and county FIPS code
	geoid10 = models.CharField(max_length=5)

	#Name of the county
	name10 = models.CharField(max_length=100)

	#Name and the translated legal/statistical area description code for county
	namelsad10 = models.CharField(max_length=100)

	#Legal/statistical area description code for county
	lsad10 = models.CharField(max_length=2)

	#FIPS 55 class code
	classfp10 = models.CharField(max_length=2)

	#MAF/TIGER feature class code
	mtfcc10 = models.CharField(max_length=5)

	#Census Combined statistical area code
	csafp10 = models.CharField(max_length=3)

	#Census metropolitan statistical area/micropolitan statistical area code
	cbsafp10 = models.CharField(max_length=5)

	#Census metropolitan divison code
	metdivfp10 = models.CharField(max_length=5)

	#2010 Census functional status
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
		verbose_name_plural =  "County Boundaries"
		app_label = 'geosera'

	def __unicode__(self):
		return self.name10

# Auto-generated `LayerMapping` dictionary for CountyBoundary model
countyboundary_mapping = {
    'statefp10' : 'STATEFP10',
    'countyfp10' : 'COUNTYFP10',
    'countyns10' : 'COUNTYNS10',
    'geoid10' : 'GEOID10',
    'name10' : 'NAME10',
    'namelsad10' : 'NAMELSAD10',
    'lsad10' : 'LSAD10',
    'classfp10' : 'CLASSFP10',
    'mtfcc10' : 'MTFCC10',
    'csafp10' : 'CSAFP10',
    'cbsafp10' : 'CBSAFP10',
    'metdivfp10' : 'METDIVFP10',
    'funcstat10' : 'FUNCSTAT10',
    'aland10' : 'ALAND10',
    'awater10' : 'AWATER10',
    'intptlat10' : 'INTPTLAT10',
    'intptlon10' : 'INTPTLON10',
    'geom' : 'MULTIPOLYGON',
}
