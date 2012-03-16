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

	reader = csv.reader(open(settings.STATE_POP_FILE), delimiter="|")

	for row in reader:
		if not row[0][0] == "#":
			state_fips = row[0]
			population = row[2]

			sql = "UPDATE states set population=%s WHERE fips_code = %s" % (population, state_fips)
			run_sql_update(conn, sql)
