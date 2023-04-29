from typing import List

from pydantic import BaseModel


class DivingSite(BaseModel):
    name: str
    min_temperature: int | None = None
    max_temperature: int | None = None
    visibility: int
    animals_in_the_water: List[str]
    scuba_diving_clubs: List[str]
    max_depth: int
    diving_time: int
    short_description: str
