"""Módulo de repositório para operações relacionadas a favoritos"""

from typing import List

from sqlalchemy.orm import Session

from app.models.favorite import Favorite
from app.services.favorite_service import FavoriteService


class FavoriteRepository:
    """Classe de repositório para gerenciar operações de banco de dados relacionadas a favoritos"""
    def __init__(self, db: Session):
        self.db = db

    def get_favorite(self, favorite_id: int) -> Favorite:
        """Faz a consulta para obter um favorito pelo ID"""
        return self.db.query(Favorite).filter(Favorite.id == favorite_id).first()

    def get_favorites(self) -> List[Favorite]:
        """Faz a consulta para obter todos os favoritos"""
        return self.db.query(Favorite).all()

    def create_favorite(self, favorite: FavoriteService) -> Favorite:
        """Faz a consulta para criar um novo favorito com os dados fornecidos"""
        db_favorite = Favorite(**favorite.db.dict())
        self.db.add(db_favorite)
        self.db.commit()
        self.db.refresh(db_favorite)
        return db_favorite

    def update_favorite(self, favorite_id: int, favorite: FavoriteService) -> Favorite:
        """Faz a consulta para atualizar um favorito existente com os dados fornecidos"""
        db_favorite = self.get_favorite(favorite_id)
        if db_favorite:
            for key, value in favorite.db.dict().items():
                setattr(db_favorite, key, value)
            self.db.commit()
            self.db.refresh(db_favorite)
        return db_favorite

    def delete_favorite(self, favorite_id: int) -> None:
        """Faz a consulta para excluir um favorito pelo ID"""
        db_favorite = self.get_favorite(favorite_id)
        if db_favorite:
            self.db.delete(db_favorite)
            self.db.commit()
