from pydantic import BaseModel
from typing import List, Optional

class FavoriteBase(BaseModel):
    url: str
    title: str

class FavoriteCreate(FavoriteBase):
    pass

class Favorite(FavoriteBase):
    id: int

    class Config:
        orm_mode = True

class FavoriteList(BaseModel):
    favorites: List[Favorite] = []