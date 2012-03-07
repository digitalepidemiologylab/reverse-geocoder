# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models

class CountyBoundary(models.Model):
	statefp10 = models.CharField(max_length=2)
	countyfp10 = models.CharField(max_length=3)
	countyns10 = models.CharField(max_length=8)
	geoid10 = models.CharField(max_length=5)
	name10 = models.CharField(max_length=100)
	namelsad10 = models.CharField(max_length=100)
	lsad10 = models.CharField(max_length=2)
	classfp10 = models.CharField(max_length=2)
	mtfcc10 = models.CharField(max_length=5)
	csafp10 = models.CharField(max_length=3)
	cbsafp10 = models.CharField(max_length=5)
	metdivfp10 = models.CharField(max_length=5)
	funcstat10 = models.CharField(max_length=1)
	aland10 = models.FloatField()
	awater10 = models.FloatField()
	intptlat10 = models.CharField(max_length=11)
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
