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

	def build_update_sql(self, data):
		sql_prefix = "UPDATE tweets SET geocoder_flag = '%s' " % self.flags['GEOSERA']
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
