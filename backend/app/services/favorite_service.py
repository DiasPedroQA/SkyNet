"""Módulo de serviço para operações relacionadas a favoritos"""

from typing import List

from sqlalchemy.orm import Session

from app.models.favorite import Favorite
from app.repositories.favorite_repo import FavoriteRepository


class FavoriteService:
    """Docstring para FavoriteService"""

    def __init__(self, db: Session):
        self.db = db
        self.favorite_repo = FavoriteRepository(db)

    def get_favorites(self) -> List[Favorite]:
        """Obtém todos os favoritos"""
        return self.favorite_repo.get_all()

    def get_favorite(self, favorite_id: int) -> Favorite:
        """Obtém um favorito pelo ID"""
        return self.favorite_repo.get_by_id(favorite_id)

    def create_favorite(self, favorite_data: dict) -> Favorite:
        """Cria um novo favorito com os dados fornecidos"""
        return self.favorite_repo.create_favorite(favorite_data)

    def update_favorite(self, favorite_id: int, favorite_data: dict) -> Favorite:
        """Atualiza um favorito existente com os dados fornecidos"""
        return self.favorite_repo.update_favorite(favorite_id, favorite_data)

    def delete_favorite(self, favorite_id: int) -> None:
        """Exclui um favorito pelo ID"""
        self.favorite_repo.delete_favorite(favorite_id)
