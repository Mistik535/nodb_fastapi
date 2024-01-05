"""
    Settings
"""

from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """ Settings class """
    main_url: str = ""

    model_config = SettingsConfigDict(
        # ищем файл .env в директории /src/
        env_file=f"{Path(__file__).resolve().parent}/.env"
    )


settings = Settings()
