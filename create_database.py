#!/usr/bin/python

# populate.py

import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT



# connect to the PostgreSQL server
conn = psycopg2.connect(host="localhost", user="postgres", password="password")
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# create a cursor
cur = conn.cursor()
		
# create database
cur.execute("create database unbabel")
	
conn.commit()
	
# close communication with the PostgreSQL
cur.close()