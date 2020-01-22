import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

query_count = '''SELECT COUNT(DISTINCT name)
FROM charactercreator_character;'''

curs.execute(query_count)

results = curs.fetchall()

print('Total characters: ', results)


query_subclass = '''SELECT COUNT(DISTINCT character_id)
FROM charactercreator_character_inventory;'''

curs.execute(query_subclass)

subclss = curs.fetchall()

print('Characters of specific subclass: ', subclss)


query_item_count = '''SELECT COUNT('item_id')
FROM armory_item;'''

curs.execute(query_item_count)

item_count = curs.fetchall()

print('Total item count: ', item_count)


query_weapons_count = '''SELECT COUNT(item_ptr_id)
FROM armory_weapon
LEFT JOIN armory_item ON item_id = item_ptr_id;'''

curs.execute(query_weapons_count)

weapons_count = curs.fetchall()

print('Number of items that are weapons: ', weapons_count)
print('Number of items that are not weapons: ', 174 - 37)
