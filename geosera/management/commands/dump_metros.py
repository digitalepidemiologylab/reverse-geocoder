from django.core.management.base import BaseCommand, CommandError
from django.utils.encoding import smart_str

from geosera.models.metro import MetropolitanStatisticalArea

class Command(BaseCommand):
	def handle(self, *args, **options):
		for p in MetropolitanStatisticalArea.objects.all():
			print p.cbsafp + '\t' + p.name.encode('ascii', 'ignore') 
