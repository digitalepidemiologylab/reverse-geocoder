import csv	

from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis.geos import Point

from geosera.models.county import CountyBoundary
from geosera.models.place import Place
from geosera.models.zipcode import ZipCode
from geosera.models.state import State
from geosera.models.metro import MetropolitanStatisticalArea

class Command(BaseCommand):
	""" Take a file with tweet_ids, longitude and latitude on the command line, and 
	reverse geocode the locations. Output is sent out using the logging system. """

	args = '<points_file_name>'
	help = 'Batch reverse geocodes'

	def handle(self, *args, **options):
		point_file_name = args[0]

		point_file_reader = csv.reader(open(point_file_name, 'rb'), delimiter='\t')

		for row in point_file_reader:
			tweet_id = row[0]
			longitude = row[1]
			latitude = row[2]

			p = Point(float(longitude), float(latitude))
			counties = CountyBoundary.objects.filter(geom__contains=p)

			response_data = {}

			if len(counties) > 0:
				response_data['county'] = counties[0].namelsad10
				response_data['county_fips'] = counties[0].geoid10
			else:
				response_data['county'] = None

			places = Place.objects.filter(geom__contains=p)

			if len(places) > 0:
				response_data['place'] = places[0].namelsad10
			else:
				response_data['place'] = None

			zipcodes = ZipCode.objects.filter(geom__contains=p)

			if len(zipcodes) > 0:
				response_data['zcta'] = zipcodes[0].zcta5ce10
			else:
				response_data['zcta'] = None

			states = State.objects.filter(geom__contains=p)

			if len(states) > 0:
				response_data['state'] = states[0].stusps10
				response_data['state_fips'] = states[0].geoid10
			else:
				response_data['state'] = None

			metros = MetropolitanStatisticalArea.objects.filter(geom__contains=p)

			if len(metros) > 0:
				response_data['metro'] = metros[0].name
				response_data['metro_code'] = metros[0].cbsafp
			else:
				response_data['metro'] = None

			print response_data
