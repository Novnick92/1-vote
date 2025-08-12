from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    ballotpedia_api_key: str | None = None
    votesmart_api_key: str | None = None
    fec_api_key: str | None = None

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

settings = Settings()
