"""Módulo principal da aplicação FastAPI"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.routers import favorites

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas as origens
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos os métodos
    allow_headers=["*"],  # Permitir todos os cabeçalhos
)

app.include_router(favorites.router, prefix="/api/v1/favorites", tags=["favorites"])

@app.get("/")
def read_root():
    """Endpoint raiz para verificar se a API está funcionando"""
    return {"message": "Welcome to the SkyNet API!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", reload=True)
