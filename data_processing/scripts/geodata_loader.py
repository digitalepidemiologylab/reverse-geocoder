#!/usr/bin/env python

import MySQLdb
import json as simplejson
import os
from mkondo import dataops
from mkondo import shunter
import settings
import logging
import logging.handlers


class TweetsLoader():
	def __init__(self,conn, flags):
		self.conn = conn
		self.flags = flags

	def run_sql_update(self, sql):
		""" Run an SQL insert or update statement. """
		cursor = self.conn.cursor()
		cursor.execute(sql)
		self.conn.commit()
		cursor.close()

	def run_sql(self, sql):
		""" Run an SQL select statement and return all the rows. """
		cursor = self.conn.cursor()
		cursor.execute(sql)
		rows = list(cursor.fetchall())
		cursor.close()
		return rows

	def update_not_geosera(self, data):
		flag = self.flags['GEOSERA_FAILED']
		sql = "UPDATE tweets SET geocoder_flag='%s' WHERE tweet_id = %s" % (flag, data['tweet_id'])
		self.run_sql_update(sql)

	def was_geocoded(self,data):
		""" Return true if any of the levels have been geocoded """
		return data['metro'] or data['county'] or data['state'] or data['place'] or data['zcta']

	def build_update_sql(self, data):
		""" Update a tweet with it's reverse geocoded information. Build and execute the SQL query. """
		sql_prefix = "UPDATE tweets SET geocoder_flag = '%s' " % self.flags['GEOSERA']
	
		if 'county_fips' in data and data['county_fips']:
			c = " ,county_fips=%s " % data['county_fips']
			sql_prefix += c

		if 'state_fips' in data and data['state_fips']:
			s = ", state_fips=%s" % data['state_fips']
			sql_prefix += s

		if 'place_fips' in data  and data['place_fips']:
			p = ", place_fips=%s" % data['place_fips']
			sql_prefix += p

		if 'zcta' in data and data['zcta']:
			z = ", zcta=%s" % data['zcta']
			sql_prefix += z

		if 'metro_code' in data and data['metro_code']:
			m = ", metro_code=%s" % data['metro_code']
			sql_prefix += m

		sql = sql_prefix + " WHERE tweet_id = %s" % data['tweet_id']
		print sql
		self.run_sql_update(sql)
		print data['tweet_id']

	def process_geocoder_data(self, data):
		if not self.was_geocoded(data):
			self.update_not_geosera(data)
		else:
			sql = self.build_update_sql(data)

if __name__ == '__main__':

	conn = MySQLdb.connect(host=settings.DATABASES['default']['HOST'], 
						user=settings.DATABASES['default']['USER'],
						passwd=settings.DATABASES['default']['PASSWORD'],
						db=settings.DATABASES['default']['NAME'])

	updater = TweetsLoader(conn, settings.GEOCODER_FLAGS)
	directories,data_files = dataops.get_all_directory_file_list(settings.GEO_DATA_SOURCE)

	for filename in data_files:
		filepath = os.path.join(settings.GEO_DATA_SOURCE, filename)
		print filepath
		if 'data' in filename:
			data_file = open(filepath, 'r')
			for line in data_file:
				data = simplejson.loads(line.split('|')[1])
				updater.process_geocoder_data(data)

			#move each file as it's done
			directory_names = shunter.extract_directory_names([filepath])
			shunter.create_directories(settings.GEO_DATA_SOURCE, directory_names)
			shunter.move_files(settings.GEO_DATA_SOURCE, [filename])
