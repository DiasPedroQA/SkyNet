from sqlalchemy.orm import Session
from typing import List
from app.models.favorite import Favorite
from app.schemas.favorite import FavoriteCreate, FavoriteUpdate

class FavoriteRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_favorite(self, favorite_id: int) -> Favorite:
        return self.db.query(Favorite).filter(Favorite.id == favorite_id).first()

    def get_favorites(self) -> List[Favorite]:
        return self.db.query(Favorite).all()

    def create_favorite(self, favorite: FavoriteCreate) -> Favorite:
        db_favorite = Favorite(**favorite.dict())
        self.db.add(db_favorite)
        self.db.commit()
        self.db.refresh(db_favorite)
        return db_favorite

    def update_favorite(self, favorite_id: int, favorite: FavoriteUpdate) -> Favorite:
        db_favorite = self.get_favorite(favorite_id)
        if db_favorite:
            for key, value in favorite.dict(exclude_unset=True).items():
                setattr(db_favorite, key, value)
            self.db.commit()
            self.db.refresh(db_favorite)
        return db_favorite

    def delete_favorite(self, favorite_id: int) -> None:
        db_favorite = self.get_favorite(favorite_id)
        if db_favorite:
            self.db.delete(db_favorite)
            self.db.commit()