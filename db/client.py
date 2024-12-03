import os
from pymongo import MongoClient
#from dotenv import dotenv_values
from dotenv import load_dotenv

load_dotenv()
#config = dotenv_values(".env")
ATLAS_URI = os.getenv("ATLAS_URI")     
db_client = MongoClient(ATLAS_URI)
#db_client = MongoClient(config["ATLAS_URI"])

