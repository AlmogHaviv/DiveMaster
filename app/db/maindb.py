import pymongo

def get_database(dbname):
   '''connect to the data base '''
   CONNECTION_STRING = "mongodb://divemaster:123456@localhost:27017"
   client = pymongo.MongoClient(CONNECTION_STRING)
   return client[dbname]


def insert_data_to_collection(database_name='test', collection_name='dive-site'):
   # Connect to a given data base database
   db = get_database(database_name)
   # Get the given collection
   users = db[collection_name]
   # Insert a single document
   result = users.insert_one([
      {
         "id": "string",
         "name": "string",
         "min_temperature": 3.12,
         "max_temperature": 3.14,
         "visibility": 23,
         "animals_in_the_water": [
            "list",
            "of",
            "names"
         ],
         "scuba_diving_club": [
            "list",
            "of",
            "names"
         ],
         "max_depth": 23,
         "diving_time": 35,
         "short_description": "string"
      }
   ])
   print(result.__inserted_id)

