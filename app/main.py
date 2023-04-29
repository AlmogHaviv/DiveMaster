from typing import Union

from fastapi import FastAPI

import service

from dbbob import maindb


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "world"}


@app.get("/items/{item_id}")
def read_item(tem_iid: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/create-new-diving-sites")
def create_new_diving_site():
    '''calling the method of creating new diving site from service'''
    maindb.insert_data_to_collection()
    return service.create_new_diving_site()

