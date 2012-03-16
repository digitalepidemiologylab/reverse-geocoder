#!/usr/bin/env python

import MySQLdb
import json as simplejson
import csv
import settings

def run_sql_update(conn, sql):
	""" Run an SQL insert or update statement. """
	cursor = conn.cursor()
	cursor.execute(sql)
	conn.commit()
	cursor.close()

if __name__ == '__main__':
	conn = MySQLdb.connect(host=settings.DATABASES['default']['HOST'], 
						user=settings.DATABASES['default']['USER'],
						passwd=settings.DATABASES['default']['PASSWORD'],
						db=settings.DATABASES['default']['NAME'])

	reader = csv.reader(open(settings.COUNTY_POP_FILE), delimiter=",")

	for row in reader:
		if not row[0][0] == "#":
			county_fips = row[0] + row[1]
			population = row[4]

			sql = "UPDATE counties set population=%s WHERE fips_code = %s" % (population, county_fips)
			run_sql_update(conn, sql)
