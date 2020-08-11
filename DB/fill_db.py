from .dl_json import dl_json_
from pymongo import MongoClient


def main_db_operation():

    #get the json from the url
    json = dl_json_("http://trumptwitterarchive.com/data/realdonaldtrump/2018.json")

    #initiate a client with the username and password for the free cluster provided by Atlas
    client = MongoClient("mongodb+srv://duchko:TryFart09@cluster0.2ylep.mongodb.net/DonalDB?retryWrites=true&w=majority")

    #insert the data
    db = client["DonalDB"]
    collection = db["DonalDB"]

    #check if the data is not already pushed
    if(collection.count() == 0):
        result = collection.insert_many(json)
    
    #close the connection
    client.close()