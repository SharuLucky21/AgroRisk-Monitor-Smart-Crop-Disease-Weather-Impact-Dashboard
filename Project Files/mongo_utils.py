from pymongo import MongoClient
from config import MONGO_URI, DB_NAME, COLLECTION_NAME

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

def insert_weather_data(region, temperature, humidity, crop, disease_risk):
    document = {
        "region": region,
        "temperature": temperature,
        "humidity": humidity,
        "crop": crop,
        "disease_risk": disease_risk
    }
    collection.insert_one(document)

def get_all_data():
    return list(collection.find())
