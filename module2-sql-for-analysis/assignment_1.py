import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

query = '''SELECT * FROM charactercreator_character
GROUP BY name'''

curs.execute(query)
