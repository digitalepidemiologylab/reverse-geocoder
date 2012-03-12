# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models

class MetropolitanStatisticalArea(models.Model):
	#Current combined statistical area code, if applicable
	csafp = models.CharField(max_length=3)
	#Current metropolitan statistical area/micropolitan statistical area code
	cbsafp = models.CharField(max_length=5)
	#Current metropolitan statistical area/micropolitan statistical area name
	name = models.CharField(max_length=100)
	#Current name and legal/statistical description
	namelsad = models.CharField(max_length=100)
	#Legal/statistical area description code
	lsad = models.CharField(max_length=2)
	#1 = Metropolitan, 2 = Micropolitan
	memi = models.CharField(max_length=1)
	#MAF/TIGER feature class code
	mtfcc = models.CharField(max_length=5)
	#Current functional status
	funcstat = models.CharField(max_length=1)
	#Land area
	aland = models.FloatField()
	#Current water area
	awater = models.FloatField()
	#Current latitude of the internal point
	intptlat = models.CharField(max_length=11)
	#Current longitude of the internal point
	intptlon = models.CharField(max_length=12)

	geom = models.MultiPolygonField(srid=4326)
	objects = models.GeoManager()

	class Meta:
		app_label = 'geosera'

	def __unicode__(self):
		return self.namelsad

# Auto-generated `LayerMapping` dictionary for MetropolitanStatisticalArea model
metropolitanstatisticalarea_mapping = {
    'csafp' : 'CSAFP',
    'cbsafp' : 'CBSAFP',
    'name' : 'NAME',
    'namelsad' : 'NAMELSAD',
    'lsad' : 'LSAD',
    'memi' : 'MEMI',
    'mtfcc' : 'MTFCC',
    'funcstat' : 'FUNCSTAT',
    'aland' : 'ALAND',
    'awater' : 'AWATER',
    'intptlat' : 'INTPTLAT',
    'intptlon' : 'INTPTLON',
    'geom' : 'MULTIPOLYGON',
}
