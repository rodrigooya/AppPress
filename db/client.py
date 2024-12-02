from pymongo import MongoClient
from dotenv import dotenv_values

config = dotenv_values(".env") 

db_client = MongoClient(config["ATLAS_URI"])

