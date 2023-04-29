from db import maindb

def create_new_diving_site():
    client = maindb.get_database('test')
    return client.name
