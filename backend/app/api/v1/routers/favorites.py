from fastapi import APIRouter, HTTPException, Depends
from typing import List
from ..schemas.favorite import FavoriteCreate, FavoriteRead
from ...services.favorite_service import FavoriteService

router = APIRouter()
favorite_service = FavoriteService()

@router.post("/", response_model=FavoriteRead)
async def create_favorite(favorite: FavoriteCreate):
    created_favorite = await favorite_service.create_favorite(favorite)
    if not created_favorite:
        raise HTTPException(status_code=400, detail="Favorite could not be created")
    return created_favorite

@router.get("/", response_model=List[FavoriteRead])
async def get_favorites():
    favorites = await favorite_service.get_all_favorites()
    return favorites

@router.get("/{favorite_id}", response_model=FavoriteRead)
async def get_favorite(favorite_id: int):
    favorite = await favorite_service.get_favorite_by_id(favorite_id)
    if not favorite:
        raise HTTPException(status_code=404, detail="Favorite not found")
    return favorite

@router.put("/{favorite_id}", response_model=FavoriteRead)
async def update_favorite(favorite_id: int, favorite: FavoriteCreate):
    updated_favorite = await favorite_service.update_favorite(favorite_id, favorite)
    if not updated_favorite:
        raise HTTPException(status_code=404, detail="Favorite not found")
    return updated_favorite

@router.delete("/{favorite_id}", response_model=dict)
async def delete_favorite(favorite_id: int):
    success = await favorite_service.delete_favorite(favorite_id)
    if not success:
        raise HTTPException(status_code=404, detail="Favorite not found")
    return {"detail": "Favorite deleted successfully"}