from pymongo import MongoClient

conn = MongoClient()
db = conn["local"]
user_coll = db["user"]
