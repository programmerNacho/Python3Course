import pymongo
from pymongo import MongoClient

my_client = MongoClient()
db = my_client.db
users = db.users

# Add one document
one_user = {"username": "Nacho",
         "password": "1234",
         "favorite_number": 19,
         "hobbies": ["videogames", "programming"]}
user_id = users.insert_one(one_user).inserted_id

# Add multiple documents
many_users = [{"username": "Second", "password": "4321"},
              {"username": "Third", "password": "9876"}]
users_inserted = users.insert_many(many_users)
users_ids = users_inserted.inserted_ids

# Count how many documents have some data
users.count_documents({"favorite_number": 19})

# Find the first document with some data
users.find_one({"username": "Nacho"})

# Find all documents with some data
# It returns a Cursor
users.find({"username:" "Second"})

# Using datetime
import datetime

current_date = datetime.datetime.now()
u_id = users.insert_one({"username": "Date Guy", "date": current_date})
old_date = datetime.datetime(2009, 8, 11)
users_found = users.count_documents({"date": {"$gt": old_date}})

# Indexes
result = users.create_index([("username", pymongo.ASCENDING)], unique=True)