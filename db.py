from pymongo import MongoClient
import os


# connect to mongo atlas cluster
mongo_client = MongoClient(os.getenv("MONGO_URI"))

# access database
weather_journal_db = mongo_client["weather_journal_db"]

# pick a code to operate on
weather_trends = weather_journal_db["weather"]

users_collection = weather_journal_db["users"]
