#
# Assignment5 Interface
#

from pymongo import MongoClient
import json
import traceback
import Assignment4_Interface_Satyam as Assignment4

DATABASE_NAME = "ddsassignment4"
COLLECTION_NAME = "businessCollection"
CITY_TO_SEARCH = "Phoenix"
MAX_DISTANCE = 20
MIN_DISTANCE = 10
MIN_REVIEW_COUNT = 25
CATEGORIES_TO_SEARCH = ["Fashion", "Food", "Cafes"]
MY_LOCATION = ["33.42315", "-111.549409"] #[LATITUDE, LONGITUDE]
SAVE_LOCATION_1 = "findBusinessBasedOnCity.txt"
SAVE_LOCATION_2 = "findBusinessBasedOnLocation.txt"


def loadBusinessTable(fileName, collection):
    try:
        page = open(fileName, "r")
        parsedJson = json.loads(page.read())
        for oneItem in parsedJson["BusinessRecords"]:
            collection.insert_one(oneItem)
    except Exception as e:
            traceback.print_exc()

def deleteDB(client, databaseName):
    client.drop_database(databaseName)

if __name__ == '__main__':
    try:
        #Getting Connection from MongoDB
        conn = MongoClient('mongodb://localhost:27017/')
        #Creating a New DB in MongoDB
        print("Creating database in MongoDB named as " + DATABASE_NAME)
        database   = conn[DATABASE_NAME]

        #Creating a collection named businessCollection in MongoDB
        print("Creating a collection in " + DATABASE_NAME + " named as " + COLLECTION_NAME)
        collection = database[COLLECTION_NAME]

        #Loading BusinessCollection from a json file to MongoDB
        print("Loading testData.json file in the " + COLLECTION_NAME + " present inside " + DATABASE_NAME)
        loadBusinessTable("testData.json", collection)
    
        #Finding All Business name and address(full_address, city and state) present in CITY_TO_SEARCH
        print("Executing FindBusinessBasedOnCity function")
        Assignment4.FindBusinessBasedOnCity(CITY_TO_SEARCH, MIN_REVIEW_COUNT, SAVE_LOCATION_1, collection)

        #Finding All Business name and address(full_address, city and state) present in radius of MY_LOCATION for CATEGORIES_TO_SEARCH
        print("Executing FindBusinessBasedOnLocation function")
        Assignment4.FindBusinessBasedOnLocation(CATEGORIES_TO_SEARCH, MY_LOCATION, MIN_DISTANCE , MAX_DISTANCE, SAVE_LOCATION_2, collection)

        #Delete database
        deleteDB(conn, DATABASE_NAME)
        conn.close()

    except Exception as detail:
        traceback.print_exc()
