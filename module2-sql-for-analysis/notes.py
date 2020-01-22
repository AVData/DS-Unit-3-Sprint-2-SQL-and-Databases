# This line is to be written in the terminal:
# pip install psycopg2-binary

import psycopg2

# note: similar to how sqlite3 module worked)
# terminal: dir(psycopg2)
# terminal: help(psycopg2.connect)


# The following can all be obtained from the element SQL
# dbname = ''
# user = ''
# password '' # do not commit this, or share
# host = '' # Port should be included or default


# pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

# Note: RPG data from SQLite to PostgreSQL
# we'd like to get the RPG data out of SQLite and insert it into PostgreSQL.
# Aka making a datapipeline, aka ETL (extract transform laod)
