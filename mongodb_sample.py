import datetime
from pymongo import MongoClient

# Connection with MongoClient
client = MongoClient('localhost', 27017)

# Getting a database (can be accessed with as property like client.my_database)
db = client['my_database']

# Getting a collection
collection = db.my_collection

# Documents
document = {
    "author": "yusa",
    "text": "My fist post",
    "tags": ["physics", "python", "deep learning"],
    "date": datetime.datetime.utcnow()
}
post_id = collection.insert_one(document).inserted_id
print(post_id)

# Find a document
post = collection.find_one({"author": "yusa"})
print(post)
