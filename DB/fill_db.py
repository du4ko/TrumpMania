from .dl_json import dl_json_
from pymongo import MongoClient


import sys


def main_db_operation():
    #to check if the db is already created and filled.
    
    #get the json from the url
    json = dl_json_("http://trumptwitterarchive.com/data/realdonaldtrump/2018.json")

    client = MongoClient("mongodb+srv://duchko:TryFart09@cluster0.2ylep.mongodb.net/DonalDB?retryWrites=true&w=majority")
    #insert the data
    db = client["DonalDB"]
    collection = db["DonalDB"]
    result = collection.insert_many(json)

    client.close()