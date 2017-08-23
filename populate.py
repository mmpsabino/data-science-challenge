#!/usr/bin/python

# populate.py

import sys
import psycopg2
import csv


try:
# connect to the PostgreSQL server, namely the Unbabel database
	conn = psycopg2.connect(host="localhost", database="unbabel", user="postgres", password="password")

# create a cursor
	cur = conn.cursor()
		
# populate table

	filesource = r'C:\...\database.csv'
	
	f = open(filesource, 'r')

	statement = """ copy public.companyx from stdin 
				csv
				header
				delimiter as ',' """
	
	cur.copy_expert(statement, f)
	
	f.close()
	
	
	conn.commit()
	
# close communication with the PostgreSQL
	cur.close()
	
except (Exception, psycopg2.DatabaseError) as error:
	print(error)

finally:

	if conn is not None:
		conn.close()
		print "Database connection closed."