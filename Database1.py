from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()

MONGO_USER = os.environ.get("MONGO_USER")
MONGO_PASS = os.environ.get("MONGO_PASS")
MONGO_CLUSTER_URL = os.environ.get("MONGO_CLUSTER_URL")

print(MONGO_USER, MONGO_PASS, MONGO_CLUSTER_URL)