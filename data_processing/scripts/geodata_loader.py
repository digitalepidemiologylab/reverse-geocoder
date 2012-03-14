#!/usr/bin/env python

import MySQLdb
import simplejson
import os
from mkondo import dataops
import settings

class TweetsLoader():
	def __init__(self,conn, flags):
		self.conn = conn
		self.flags = flags
		self.state_fips_cache = None

	def run_sql(self, sql):
		cursor = self.conn.cursor()
		cursor.execute(sql)
		rows = list(cursor.fetchall())
		cursor.close()
		return rows

	def update_not_geosera(self, data):
		flag = self.flags['GEOSERA_FAILED']
		sql = "UPDATE tweets SET geocoder_flag='%s' WHERE tweet_id = %s" % (flag, data['tweet_id'])
		print sql

	def was_geocoded(self,data):
		""" Return true if at least one of the levels has been reverse geocoded."""
		return data['metro'] and data['county'] and data['state'] and data['place'] and data['zcta']

	def populate_state_fips(self):
		sql = "SELECT fips_code FROM states";

		fips_codes = self.run_sql(sql)
		for code in fips_codes:
			self.state_fips_cache[code] = True
		raise Exception('Not implemented')

	def add_state(self, fips, two_letter_abbr):
		if self.state_fips is None:
			self.populate_state_fips()
		
		if fips not in self.state_fips_cache:
			sql = "INSERT INTO states fips_code = %s, two_letter_code = %s" % (fips, two_letter_abbr)
			state_fips_cache[fips] = True

	def add_county(self, fips, county_name, state_two_letter):
		pass

	def add_zcta(self, zipcode, state_two_letter):
		pass

	def build_update_sql(self, data):
		sql_prefix = "UPDATE tweets SET geocoder_flag = '%s' " % self.flags['GEOSERA']
		state_two_letter = None
		if 'state_fips' and 'state' in data:
			add_state(data['state_fips'], data['state'])
			state_two_letter = data['state']
		if 'county_fips' and 'county' in data:
			add_county(data['county_fips'], data['county'], state_two_letter)
		if 'zcta' in data:
			add_zcta(data['zcta'], state_two_letter)

		sql += "WHERE tweet_id = %s" % data['tweet_id']

	def process_geocoder_data(self, data):
		if not self.was_geocoded(data):
			self.update_not_geosera(data)
		else:
			sql = build_update_sql(data)

if __name__ == '__main__':

	conn = MySQLdb.connect(host=settings.DATABASES['default']['HOST'], 
						user=settings.DATABASES['default']['USER'],
						passwd=settings.DATABASES['default']['PASSWORD'],
						db=settings.DATABASES['default']['NAME'])

	updater = TweetsLoader(conn, settings.GEOCODER_FLAGS)
	directories,data_files = dataops.get_all_directory_file_list(settings.GEO_DATA_SOURCE)

	#insert data into database

	for filename in data_files:
		filepath = os.path.join(settings.GEO_DATA_SOURCE, filename)
		if 'data' in filename:
			data_file = open(filepath, 'r')
			for line in data_file:
				data = simplejson.loads(line.split('|')[1])
				updater.process_geocoder_data(data)
				
	#geocoded flag
