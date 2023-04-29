from typing import Union

from fastapi import FastAPI

import service

from dbbob import maindb

from pydantic import BaseModel

from dto import divingSiteDto

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "world"}


@app.post("/create-new-diving-sites")
async def create_dive_site(site: divingSiteDto.DivingSite):
    maindb.insert_data_to_collection(site)
    return site
