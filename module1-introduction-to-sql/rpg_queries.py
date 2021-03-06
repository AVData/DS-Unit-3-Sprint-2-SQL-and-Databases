import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3') # Connetion to database created
curs = conn.cursor()                     # Curser instatiated as curs for db

query_count = '''SELECT COUNT(DISTINCT name)
FROM charactercreator_character;''' # Queries are created similarly
                                    # to docstrins, in that they live in the '''

curs.execute(query_count)           # In order to execute a query in a db, use
                                    # method .execute(qurey_var)

results = curs.fetchall()           # The method .fetchall() returns the results
                                    # from the executed query. Here we are setting
                                    # it as the var 'results'

print('\n', 'Total characters: ', results)  # But in order to acutally see your
                                            # query in your terminal, you need
                                            # to do a print function.


# the following code is a reitteation of the above.  See below to know how to
# commit this to your db and exit.

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

# when all of the queries above are performed you can simply do a conn.commit()
# and a curs.exit() to exit the db.
