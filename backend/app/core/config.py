from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    MONGO_URI:str
    DATABASE_NAME:str

    QDRANT_URL:str
    QDRANT_API_KEY:str

    OLLAMA_BASE_URL:str
    EMBEDDING_MODEL:str
    LLM_MODEL:str

    model_config =SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

settings = Settings()