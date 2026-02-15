"""Módulo de dependências para a API"""

from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repositories.favorite_repo import FavoriteRepo


def get_favorite_repo(db: Session = Depends(get_db)) -> FavoriteRepo:
    """Dependência para obter uma instância do repositório de favoritos"""
    return FavoriteRepo(db)
