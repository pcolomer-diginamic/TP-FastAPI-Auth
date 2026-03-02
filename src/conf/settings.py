"""Constans in full maj. (PEP 8)"""

from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    
    # ============================================================================
    # INFORMATIONS DE L'APPLICATION
    # ============================================================================
    
    CONNECTOR: str
    USER: str
    PASSWORD: str
    HOST: str
    PORT: int
    DB_NAME: str
    
    # ============================================================================
    # PROPRIETES CALCULEES
    # ============================================================================

    @property
    def CONNECTION_STRING(self) -> str:
        return (
            f"{self.CONNECTOR}://"
            f"{self.USER}:{self.PASSWORD}@"
            f"{self.HOST}:{self.PORT}/"
            f"{self.DB_NAME}"
        )
        
    # ============================================================================
    # CONFIGURATION PYDANTIC
    # ============================================================================

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=True
    )


# ============================================================================
# INSTANCE GLOBALE (SINGLETON)
# ============================================================================

@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()