from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()

MONGO_USER = os.environ.get("MONGO_USER")
MONGO_PASS = os.environ.get("MONGO_PASS")
MONGO_CLUSTER_URL = os.environ.get("MONGO_CLUSTER_URL")

print(MONGO_USER, MONGO_PASS, MONGO_CLUSTER_URL)


#url=mongodb+srv://ajochoa03:Naruto16@Leaf16@cluster0.qmtvcxo.mongodb.net/?appName=Cluster0

#client = MongoClient(url)
#print(client)

db = client["water_quality_data"]
robot1 = db["asv1"]

print(f"Using database {db} and collection {robot1}.")

obs1 = {"temp":92,
        "salinity":35,
        "pH":6.5,
        "oxygen":7.2,
        "notes":"good"}
result1 = robot1.insert_one(obs1)

listObs = [
        {"temp":92,"salinity":35,"pH":6.5,"oxygen":7.2,"notes":"good"},
        {"temp":93,"salinity":35,"pH":6.5,"oxygen":7.2,"notes":"good"},
        {"temp":94,"salinity":35,"pH":6.5,"oxygen":7.2,"notes":"good"}
        ]

result2 = robot1.insert_many(listObs)

#Other methods:

doc = robot1.find_one()

for obs in robot1.find({"temp":{"$gt":28}}):
        print("Hot water",obs)