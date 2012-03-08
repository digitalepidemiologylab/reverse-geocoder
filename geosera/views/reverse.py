from django.shortcuts import render
from django.http import HttpResponse
from django.utils import simplejson

from django.contrib.gis.geos import Point

from geosera.models.county import CountyBoundary
from geosera.models.place import Place
from geosera.models.zipcode import ZipCode

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

	return HttpResponse(simplejson.dumps(response_data), mimetype='application/json')
