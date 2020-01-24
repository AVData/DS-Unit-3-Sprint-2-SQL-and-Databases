# Answers for Module 3 Assignment


## Describe two situations where:
- When is a relational database is appropriate:
    - 

- When is a non-relational database is appropriate:




terminal command:
`mongo "mongodb+srv://cluster0-ji4lx.mongodb.net/test"  --username Avargas`

helpful link to use mongo:
https://docs.atlas.mongodb.com/tutorial/insert-data-into-your-cluster/#moving-forward


Used the following command in the terminal to connect to the MongoDB Shell
`mongo "mongodb+srv://cluster0-ji4lx.mongodb.net/test"  --username Avargas`

Should result in an enter password request; insert password from the
MongoDB user tab.  You might need to update the user password in the user profile
password =

The MongoDB shell on terminal is different from using the python shell; in the
MongoDB shell the equivalent of:

client = pymongo.MongoClient(
    "mongodb+srv://admin:HfAXLeBx3nWPkKwV@cluster0-hvfwb.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

Is simply running:
`mongo "mongodb+srv://cluster0-ji4lx.mongodb.net/test"  --username Avargas`

which should connect you to the mongodb shell.

Once in the MongoDB shell you can begin with the following commands:

`db.help()`

Which will provide you help with the db methods available through the shell

Running our first method call on the db.test:
run the following code in the terminal and it should allow you to create a new "collection"

`db.test.insertOne({'x': 1})``

running `show collections` should provide us with the db test created

Run the following dictionaries

`loris_doc = {
    'favorite_animal': 'peacock',
    'favorite_color': 'blue',
    'favorite_number': 7
}

jons_doc = {
    'favorite_animal': 'narwhal',
    'favorite_color': 'blue',
    'favorite_number': 24
}

emmas_doc={
    'favorite_animal':'panther',
    'favorite_color': 'purple',
    'favorite_number': 2
}

rays_doc = {
    'favorite_animal': 'wolf',
    'favorite_color': 'blue',
    'favorite_number': 16
}

baisali_doc={
    'favorite_animal':'elephant',
    'favorite_color': 'red',
    'favorite_number': 2
}

juds_doc = {
    'favorite_animal': 'liger',
    'favorite_color': 'blellow',
    'favorite_number': 42,
    'favorite_direction': 'Weast'
}

jans_doc = {
    'favorite_city': 'rotterdam',
    'favorite_color': 'green',
    'favorite_sport': 'football'
}

faraazs_doc = {
    'favorite_animal': 'ring-tailed lemur',
    'favorite_color': 'forest green',
    'favorite_restaurant': 'in-n-out'
}`

Then run the following list

`all_docs = [loris_doc, jons_doc, emmas_doc, rays_doc, baisali_doc, juds_doc,
            jans_doc, faraazs_doc]`

and then insert the list 'all_docs' into your database with the
`.insertMany()` method

with the `.find()` method you can see what is in the db
