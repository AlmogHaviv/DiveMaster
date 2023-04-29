import pymongo
from dto import divingSiteDto


def get_database(dbname):
    """connect to the data base"""
    CONNECTION_STRING = "mongodb://divemaster:123456@localhost:27017"
    client = pymongo.MongoClient(CONNECTION_STRING)
    return client[dbname]


def insert_data_to_collection(
    site: divingSiteDto.DivingSite, database_name="test", collection_name="dive-site"
):
    # Connect to a given data base database
    db = get_database(database_name)
    # Get the given collection
    users = db[collection_name]
    # Insert a single document
    result = users.insert_one(
        {
            "name": site.name,
            "min_temperature": site.min_temperature,
            "max_temperature": site.max_temperature,
            "visibility": site.visibility,
            "animals_in_the_water": site.animals_in_the_water,
            "scuba_diving_club": site.scuba_diving_clubs,
            "max_depth": site.max_depth,
            "diving_time": site.diving_time,
            "short_description": site.short_description,
        }
    )
    print(result.inserted_id)
