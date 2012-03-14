#!/usr/bin/env python

import MySQLdb
import simplejson
import os
from mkondo import dataops
import settings

class TweetsUpdater():
	def __init__(conn, flags):
		self.conn = conn
		self.flags = flags

	def update_not_geosera(self, data):
		flag = self.flags['GEOSERA_FAILED']
		sql = "UPDATE tweets SET geocoder_flag='%s' WHERE tweet_id = %s" % (flag, data['tweet_id'])
		print sql

def update_not_geosera(conn, data):

def was_geocoded(data):
	""" Return true if at least one of the levels has been reverse geocoded."""
	return data['metro'] or data['county'] or data['state'] or data['place'] or data['zcta']

def process_geocoder_data(conn, data):
	if not was_geocoded(data):
		update_not_geosera(conn, data):
	else:

if __name__ == '__main__':

	conn = MySQLdb.connect(host=settings.DATABASES['default']['HOST'], 
						user=settings.DATABASES['default']['USER'],
						passwd=settings.DATABASES['default']['PASSWORD'],
						db=settings.DATABASES['default']['NAME'])

	directories,data_files = dataops.get_all_directory_file_list(settings.GEO_DATA_SOURCE)

	#insert data into database

	for filename in data_files:
		filepath = os.path.join(settings.GEO_DATA_SOURCE, filename)
		if 'data' in filename:
			data_file = open(filepath, 'r')
			for line in data_file:
				data = simplejson.loads(line.split('|')[1])

				process_geocoder_data(conn, data)
				
	#geocoded flag
