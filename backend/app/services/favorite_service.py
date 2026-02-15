from typing import List
from sqlalchemy.orm import Session
from app.models.favorite import Favorite
from app.repositories.favorite_repo import FavoriteRepository

class FavoriteService:
    def __init__(self, db: Session):
        self.db = db
        self.favorite_repo = FavoriteRepository(db)

    def get_favorites(self) -> List[Favorite]:
        return self.favorite_repo.get_all()

    def get_favorite(self, favorite_id: int) -> Favorite:
        return self.favorite_repo.get_by_id(favorite_id)

    def create_favorite(self, favorite_data: dict) -> Favorite:
        return self.favorite_repo.create(favorite_data)

    def update_favorite(self, favorite_id: int, favorite_data: dict) -> Favorite:
        return self.favorite_repo.update(favorite_id, favorite_data)

    def delete_favorite(self, favorite_id: int) -> None:
        self.favorite_repo.delete(favorite_id)