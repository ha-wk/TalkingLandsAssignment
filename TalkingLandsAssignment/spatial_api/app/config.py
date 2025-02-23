from pydantic import BaseSettings

# Load environment variables securely
class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://user:password@localhost/spatial_db"

    class Config:
        env_file = ".env"  # Load environment variables from .env file

settings = Settings()
