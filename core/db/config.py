from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    POSTGRES_URL: str

    model_config = SettingsConfigDict(
        env_File=".env",
        ignore=True
    )

settings = Settings()