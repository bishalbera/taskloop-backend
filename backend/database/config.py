from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str
    database_username: str
    database_password: str
    database_name: str


    class Config:
        env_file = ".env"


settings = Settings()
