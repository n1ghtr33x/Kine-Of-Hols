from pydantic_settings import BaseSettings  # изменённый импорт
from functools import lru_cache

class Settings(BaseSettings):
    HOST: str
    PORT: int
    VERSION: str
    DATABASE_URL: str
    DEBUG: bool = False

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()
