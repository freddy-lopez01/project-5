from pymongo import MongoClient
import os 

client = MongoClient('mongodb://' + os.enviorn["MONGODB_HOSTNAME"], 27017)

db = client.mydb

collection = db.table

def insert_brevet(brevet_dist, start_time, control_dist):
    #db.insert_one()
    res = collection.insert_one({
        "brevet_dist": brevet_dist,
        "start_time": start_time,
        "control_dist": control_dist})
    _id = res.inserted_id
    
    return str(_id)



def get_brevet():
    #db.find_one
    lists = collection.find_one().sort("_id", -1).limit(1)
    
    for ls in lists:

        return ls["brevet_dist"], ls["start_time"], ls["control_dist"]

