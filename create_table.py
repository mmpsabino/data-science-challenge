#!/usr/bin/python

# create_table.py

import sys
import psycopg2


	
queries = """create type status as enum ('issuable', 'issued', 'paid', 'not_invoiced', 'overdue', 'voided');
				
			 create type revenue_type as enum ('SPC', 'SPE', 'OTS', 'TOP', 'REF', 'TRI', 'DIS');

			 create table companyx (
					"Transaction-ID" varchar(255) PRIMARY KEY,
					"Created at" date NOT NULL,
					"Start Date" date,
					"End Date" date,
					"Amount USD" float,
					"Status" status,
					"Revenue Type" revenue_type);"""

	

try:
# connect to the PostgreSQL server, namely the Unbabel database
	conn = psycopg2.connect(host="localhost", database="unbabel", user="postgres", password="password")

# create a cursor
	cur = conn.cursor()
		
# creating table
		
	cur.execute(queries)
	
	conn.commit()
	
# close communication with the PostgreSQL
	cur.close()
	
except (Exception, psycopg2.DatabaseError) as error:
	print(error)

finally:

	if conn is not None:
		conn.close()
		print "Database connection closed."