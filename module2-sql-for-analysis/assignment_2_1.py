# This line is to be written in the terminal:
# pip install psycopg2-binary

import psycopg2
import sqlite3

# note: similar to how sqlite3 module worked)
# terminal: dir(psycopg2)
# terminal: help(psycopg2.connect)


# The following can all be obtained from the element SQL
dbname = ''
user = ''
password = '' # do not commit this, or share
host = '' # Port should be included or default


pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

# Note: RPG data from SQLite to PostgreSQL
# we'd like to get the RPG data out of SQLite and insert it into PostgreSQL.
# Aka making a datapipeline, aka ETL (extract transform laod)\

pg_curs = pg_conn.cursor()

create_table_statement = """
CREATE TABLE test_table (
  id        SERIAL PRIMARY KEY,
  name  varchar(40) NOT NULL,
  data    JSONB
);
"""
pg_curs.execute(create_table_statement)
pg_conn.commit()

query = "SELECT * FROM test_table;"
pg_curs.execute(query)
pg_curs.fetchall()


sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

row_count = 'SELECT * FROM charactercreator_character'
sl_curs.execute(row_count).fetchall()

get_characters = 'SELECT * FROM charactercreator_character'
characters = sl_curs.execute(get_characters).fetchall()

sl_curs.execute('PRAGMA table_info(charactercreator_character);').fetchall()

create_charactor_table = """
CREATE TABLE charactercreator_character (
  character_id SERIAL PRIMARY KEY,
  name VARCHAR(30),
  level INT,
  exp INT,
  hp INT,
  strength INT,
  intelligence INT,
  dexterity INT,
  wisdom INT
);
"""
pg_curs.execute(create_charactor_table)
pg_conn.commit()

show_tables = """
SELECT
   *
FROM
   pg_catalog.pg_tables
WHERE
   schemaname != 'pg_catalog'
AND schemaname != 'information_schema';
"""

pg_curs.execute(show_tables)
pg_curs.fetchall()

example_insert = """
INSERT INTO charactercreator_character
(name, level, exp, hp, strength, intelligence, dexterity, wisdom)
VALUES """ + str(characters[0][1:]) + ";"

print(example_insert)

for character in characters:
  insert_character = """
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES """ + str(character[1:]) + ";"
  pg_curs.execute(insert_character)

pg_curs.execute('SELECT * FROM charactercreator_character')
pg_curs.fetchall()
pg_conn.commit()

pg_curs.execute('SELECT * FROM charactercreator_character')
pg_characters = pg_curs.fetchall()

for character, pg_character in zip(characters, pg_characters):
    assert character == pg_character

pg_curs.close()
pg_conn.close()
