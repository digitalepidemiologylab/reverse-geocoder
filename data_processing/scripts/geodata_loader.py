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
		print sql

	def was_geocoded(self,data):
		""" Return true if at least one of the levels has been reverse geocoded."""
		return data['metro'] and data['county'] and data['state'] and data['place'] and data['zcta']

	def populate_state_fips(self):
		""" To prevent us from extra queries on the database, we cache the state fips codes that are 
		already in the database. """

		sql = "SELECT fips_code FROM states";

		fips_codes = self.run_sql(sql)
		for code in fips_codes:
			self.state_fips_cache[code] = True

	def add_state(self, fips, two_letter_abbr):
		""" If a state is not already in our database, add it. Use the state fips codes cache to 
		prevent extra database queries. """

		if self.state_fips is None:
			self.populate_state_fips()
		
		if fips not in self.state_fips_cache:
			sql = "INSERT INTO states fips_code = %s, two_letter_code = %s" % (fips, two_letter_abbr)
			self.run_sql_update(sql)
			#Add the state's FIPS code to the cache.
			state_fips_cache[fips] = True

	def add_county(self, fips, county_name, state_two_letter):
		""" Add a county if it doesn't already exist. """
		sql = "SELECT fips_code FROM counties WHERE fips_code = %s" % fips
		result = run_sql(sql)
		if len(result) < 1:
			sql = "INSERT INTO counties fips_code=%s, name=%s, state_two_letter=%s" % (fips_code, 
								county_name, state_two_letter)
			self.run_sql_update(sql)

	def add_zcta(self, zipcode, state_two_letter):
		""" Add a zipcode tabulation area if it does not already exist. """
		sql = "SELECT zipcode from zctas WHERE zipcode = %s" % zipcode
		result = run_sql(sql)
		if len(result) < 1:
			sql = "INSERT into zctas zipcode=%s, state_two_letter=%s " % (zipcode, state_two_letter)
			self.run_sql_update(sql)

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
