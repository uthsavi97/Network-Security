import os
import sys
import json
import certifi
import pandas as pd
import numpy as np
from pymongo import MongoClient
from dotenv import load_dotenv
from networksecurity.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

# Load environment variables
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
if not MONGO_DB_URL:
    raise ValueError("MONGO_DB_URL not found in environment variables")

ca = certifi.where()

class NetworkDataExtract:
    def __init__(self):
        try:
            self.mongo_client = MongoClient(MONGO_DB_URL, tlsCAFile=ca)
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def csv_to_json_convertor(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_mongodb(self, records, database, collection):
        try:
            db = self.mongo_client[database]
            coll = db[collection]
            coll.insert_many(records)
            return len(records)
        except Exception as e:
            raise NetworkSecurityException(e, sys)

if __name__ == "__main__":
    FILE_PATH = "Network_Data/phishingData.csv"  # Corrected typo in file name
    DATABASE = "uthsavi97"
    COLLECTION = "NetworkData"

    network_obj = NetworkDataExtract()
    try:
        records = network_obj.csv_to_json_convertor(file_path=FILE_PATH)
        print(records)
        no_of_records = network_obj.insert_data_mongodb(records, DATABASE, COLLECTION)
        print(f"Inserted {no_of_records} records into MongoDB")
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
