"""
    Settings
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """ Settings class """
    main_url: str

    def __init__(self, main_url):
        super().__init__()
        self.main_url = main_url


settings = Settings("google.com")
