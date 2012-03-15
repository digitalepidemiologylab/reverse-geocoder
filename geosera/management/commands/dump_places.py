from django.core.management.base import BaseCommand, CommandError
from django.utils.encoding import smart_str

from geosera.models.place import Place 

class Command(BaseCommand):
	def handle(self, *args, **options):
		for p in Place.objects.all():
			print p.geoid10 + '\t' + p.namelsad10.encode('ascii', 'ignore') 
