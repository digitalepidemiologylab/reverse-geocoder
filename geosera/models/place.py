# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models

class Place(models.Model):
	statefp10 = models.CharField(max_length=2)
	placefp10 = models.CharField(max_length=5)
	placens10 = models.CharField(max_length=8)
	geoid10 = models.CharField(max_length=7)
	name10 = models.CharField(max_length=100)
	namelsad10 = models.CharField(max_length=100)
	lsad10 = models.CharField(max_length=2)
	classfp10 = models.CharField(max_length=2)
	pcicbsa10 = models.CharField(max_length=1)
	pcinecta10 = models.CharField(max_length=1)
	mtfcc10 = models.CharField(max_length=5)
	funcstat10 = models.CharField(max_length=1)
	aland10 = models.FloatField()
	awater10 = models.FloatField()
	intptlat10 = models.CharField(max_length=11)
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
