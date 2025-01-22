import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MANGO_DB_URL = os.getenv("MANGO_DB_URL")
print(MANGO_DB_URL)

import certifi
ca=certifi.where()

import pandas as pd
import numpy as np
import pymango
from networksecurity.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def cv_to_json_convertor(self,file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def insert_data_mangodb(self,records,database,collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records

            self.mango_client=pymango.MangoClient(MANGO_DB_URL)
            self.database = self.mango_client(self.database)

            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)
            return(len(self.records))
        except Exception as e:
            raise NetworkSecurityException(e,sys)

 if __name__="__main__":
F       