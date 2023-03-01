from pymongo import Mongoclient
import os

client = MongoClient('mongodb://' + os.enviorn['MONGODB_HOSTNAME'], 27017)
db = client.mydb

def insert_brevet(brevet_dist, start_time, controls):
    #db.insert_one
    pass

def get_brevet():
    #db.find_one
    return brevet_dist, start_time, controls
