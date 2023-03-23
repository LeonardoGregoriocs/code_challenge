from typing import List
from pydantic import BaseModel

class RoomSchema(BaseModel):
    wall_height: float
    wall_length: float
    amount_of_doors: int | None = None
    amount_of_windows: int | None = None

class Measurements(BaseModel):
    measurements: List[RoomSchema]

    class Config:
        orm_mode = True
