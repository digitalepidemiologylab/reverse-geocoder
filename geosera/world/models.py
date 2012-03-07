
# This is an auto-generated Django model module created by ogrinspect.
# To generate this model, I did this:
# python manage.py ogrinspect world/data/TM_WORLD_BORDERS-0.3.shp WorldBorders
# Manual changes have been made. 

from django.contrib.gis.db import models

class WorldBorders(models.Model):
	fips = models.CharField(max_length=2)
	iso2 = models.CharField(max_length=2)
	iso3 = models.CharField(max_length=3)
	un = models.IntegerField()
	name = models.CharField(max_length=50)
	area = models.IntegerField()
	pop2005 = models.IntegerField()
	region = models.IntegerField()
	subregion = models.IntegerField()
	lon = models.FloatField()
	lat = models.FloatField()

	#GeoDjango-specific: a geometry field and overriding the default manager with a GeoManager instance. 
	geom = models.MultiPolygonField()
	objects = models.GeoManager()

	class Meta:
		verbose_name_plural = "World Borders"	

	def __unicode__(self):
		return self.name
