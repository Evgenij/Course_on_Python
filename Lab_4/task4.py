import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.database
collections = db.collections

post_1 = {
     'title': 'Pice and War',
     'content': '_',
     'author': 'Lev Tolstoy'
    }
post_2 = {
     'title': 'Evgeniy Onegin',
     'content': '~',
     'author': 'Pyskin'
    }
post_3 = {
     'title': 'Died Soul)',
     'content': '/',
     'author': 'Gogol'
    }

all_posts = collections.insert_many([post_1, post_2, post_3])
print('Multiple posts: {0}'.format(all_posts.inserted_ids))
