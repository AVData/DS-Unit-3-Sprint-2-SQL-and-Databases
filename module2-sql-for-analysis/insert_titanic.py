import sqlite3
import psycopg2
import pandas as pd


dbname = ''
user = ''
password = '' # do not commit this, or share
host = '' # Port should be included or default

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
pg_curs = pg_conn.cursor()

create_table_statement = '''
CREATE TABLE titanic_tbl (
id SERIAL NOT NULL PRIMARY KEY,
Survived integer,
Pclass integer,
Name text,
Sex text,
Age real,
Siblings_Spouses_Aboard integer,
Parents_Children_Aboard integer,
Fare money);
'''

pg_curs.execute(create_table_statement)

titanic_df = pd.read_csv('titanic.csv')

sl_conn = sqlite3.connect('titanic.sqlite3')
sl_curs = sl_conn.cursor()

titanic_df['Name'] = titanic_df['Name'].str.replace("'", "")

titanic_df.to_sql('titanic', sl_conn, if_exists='replace')

sl_curs = sl_conn.cursor()

peoples = sl_curs.execute('SELECT * FROM titanic;').fetchall()
peoples

for people in peoples:
  insert_people = """
    INSERT INTO titanic_tbl
    (id, Survived, Pclass, Name, Sex, Age, Siblings_Spouses_Aboard, Parents_Children_Aboard, Fare)
    VALUES """ + str(people[:]) + ';'
  pg_curs.execute(insert_people)

pg_curs.execute('SELECT * FROM titanic_tbl;')
pg_curs.fetchone()

pg_curs.close()
pg_conn.commit()
pg_conn.close()
