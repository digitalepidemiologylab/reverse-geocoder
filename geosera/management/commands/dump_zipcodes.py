from django.core.management.base import BaseCommand, CommandError

from geosera.models.zipcode import ZipCode

class Command(BaseCommand):
	def handle(self, *args, **options):
		for z in ZipCode.objects.all():
			print z.geoid10
