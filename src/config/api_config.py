from pydantic import SecretStr, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    tomorrow_api_key: SecretStr = Field(
    validation_alias="API_KEY_TOMORROW_OI"
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


api_settings = Settings()