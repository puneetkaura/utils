__author__ = 'pkaura'
import os

import requests
from peewee import *
'''
Steps:
- Run a loop on the url :
- Get the data
- Save username,name, phunt_id, votes_count, posts_count, maker_of_count, followers_count, followings_count, created_at to SQLite
- Give queries for highest number of upvotes
'''

db = SqliteDatabase('my_app.db')

# Connect to our database.
db.connect()

class BaseModel(Model):
    """A base model that will use our Sqlite database."""
    class Meta:
        database = db

class PHData(BaseModel):
    phunt_id = IntegerField()
    name = CharField()
    username = CharField()
    votes_count = IntegerField()
    posts_count = IntegerField()
    maker_of_count = IntegerField()
    followers_count = IntegerField()
    followings_count = IntegerField()
    # created_at = DateField()

# class PH401(BaseModel):


# Create the tables.
# db.create_tables([PHData])

batch_size = 5
start = 1
finish = 100
base_url = "https://api.producthunt.com/v1/users/"
i=start

bearer_token = os.environ['PH_TOKEN']
print bearer_token

while i < finish :
    url = base_url + str(i)
    # r = requests.get(url, headers={'Authorization': 'Bearer 15f6324663cf73a5fc51612a9d4eb1e696a8cc2ff7ed67d1ba733c0f33c7136d})
    r = requests.get(url, headers={'Authorization': bearer_token})

    if  r.status_code == 200 :
        phd = r.json()['user']
        phunt_data = PHData(phunt_id=phd['id'], name=phd['name'], username=phd['username'], votes_count=int(phd['votes_count']), \
                     posts_count = int(phd['posts_count']), maker_of_count=int(phd['maker_of_count']), followers_count=int(phd['followers_count']), \
                     followings_count = int(phd['followings_count']),)

        phunt_data.save()
        print i, phunt_data.name
        i += 1
    else :
        print i, r.status_code
        i += 1




