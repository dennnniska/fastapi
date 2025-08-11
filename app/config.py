from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "postgresql+psycopg2://postgres:123@localhost:5432/postgres"
    
    class Config:
        env_file = ".env"

settings = Settings()