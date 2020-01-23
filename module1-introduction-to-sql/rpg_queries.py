import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

query_count = '''SELECT COUNT(DISTINCT name)
FROM charactercreator_character;'''

curs.execute(query_count)

results = curs.fetchall()

print('\n', 'Total characters: ', results)


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

query_items_not_weapons = '''
SELECT COUNT(DISTINCT item_id) - COUNT(DISTINCT item_ptr_id)
FROM armory_item, armory_weapon
'''

print('Number of items that are not weapons: ', query_items_not_weapons, '\n')


query_items_per_character = '''SELECT character.name, item.name
FROM charactercreator_character AS character,
charactercreator_character_inventory AS inventory,
armory_item AS item
WHERE character.character_id = inventory.character_id
AND inventory.item_id = item.item_id
LIMIT 20;'''

curs.execute(query_items_per_character)

items_per_character = curs.fetchall()

print('Table of first 20 rows for items/character: ', '\n',
items_per_character, '\n')


query_weapons_per_character = '''SELECT character.name, weapon.item_ptr_id
FROM charactercreator_character AS character,
charactercreator_character_inventory AS inventory,
armory_weapon AS weapon
WHERE character.character_id = inventory.character_id
AND inventory.item_id = weapon.item_ptr_id
LIMIT 20;'''

curs.execute(query_weapons_per_character)

weapons_per_character = curs.fetchall()

print('Table of first 20 rows of weapons/character: ', '\n',
weapons_per_character, '\n')
