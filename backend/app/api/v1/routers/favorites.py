"""Módulo de roteadores para operações relacionadas a favoritos"""

from backend.app.api.v1.schemas.favorite import FavoriteBase
from fastapi import APIRouter, HTTPException

router = APIRouter()
favorite_service = FavoriteBase()

@router.post("/", response_model=FavoriteBase)
async def create_favorite(favorite: FavoriteBase):
    """Função para criar um novo favorito"""
    created_favorite = await favorite_service.create_favorite(favorite)
    if not created_favorite:
        raise HTTPException(status_code=400, detail="Favorite could not be created")
    return created_favorite

@router.get("/", response_model=list[FavoriteBase])
async def get_favorites():
    """Função para obter todos os favoritos"""
    favorites = await favorite_service.get_all_favorites()
    return favorites

@router.get("/{favorite_id}", response_model=FavoriteBase)
async def get_favorite(favorite_id: int):
    """Função para obter um favorito pelo ID"""
    favorite = await favorite_service.get_favorite_by_id(favorite_id)
    if not favorite:
        raise HTTPException(status_code=404, detail="Favorite not found")
    return favorite

@router.put("/{favorite_id}", response_model=FavoriteBase)
async def update_favorite(favorite_id: int, favorite: FavoriteBase):
    """Função para atualizar um favorito existente"""
    updated_favorite = await favorite_service.update_favorite(favorite_id, favorite)
    if not updated_favorite:
        raise HTTPException(status_code=404, detail="Favorite not found")
    return updated_favorite

@router.delete("/{favorite_id}", response_model=dict)
async def delete_favorite(favorite_id: int):
    """Função para excluir um favorito"""
    success = await favorite_service.delete_favorite(favorite_id)
    if not success:
        raise HTTPException(status_code=404, detail="Favorite not found")
    return {"detail": "Favorite deleted successfully"}
    return {"detail": "Favorite deleted successfully"}
