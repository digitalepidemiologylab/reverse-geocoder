from django.shortcuts import render
from django.http import HttpResponse
from django.utils import simplejson

from django.contrib.gis.geos import Point

from geosera.models.county import CountyBoundary
from geosera.models.place import Place
from geosera.models.zipcode import ZipCode
from geosera.models.state import State
from geosera.models.metro import MetropolitanStatisticalArea

def reverse(request, lat, lng):
	response_data = {}
	response_data['lat'] = lat
	response_data['long'] = lng

	p = Point(float(lng), float(lat))
	counties = CountyBoundary.objects.filter(geom__contains=p)

	if len(counties) > 0:
		response_data['county'] = counties[0].name10
	else:
		response_data['county'] = None

	places = Place.objects.filter(geom__contains=p)

	if len(places) > 0:
		response_data['place'] = places[0].name10
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
	else:
		response_data['state'] = None

	metros = MetropolitanStatisticalArea.objects.filter(geom__contains=p)

	if len(metros) > 0:
		response_data['metro'] = metros[0].name
	else:
		response_data['metro'] = None

	return HttpResponse(simplejson.dumps(response_data), mimetype='application/json')
