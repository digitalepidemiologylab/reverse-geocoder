from django.core.management.base import BaseCommand, CommandError
from django.utils.encoding import smart_str

from geosera.models.county import CountyBoundary

class Command(BaseCommand):
	def handle(self, *args, **options):
		for c in CountyBoundary.objects.all():
			print c.geoid10 + '\t' + c.name10.encode('ascii', 'ignore') + '\t' + c.statefp10
