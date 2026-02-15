from pydantic import BaseSettings


class Settings(BaseSettings):
    # Configurações do banco de dados
    DATABASE_URL: str
    # Outras configurações podem ser adicionadas aqui

    class Config:
        env_file = ".env"

settings = Settings()
