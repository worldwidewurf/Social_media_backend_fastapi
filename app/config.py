from pydantic import BaseSettings

class Settings(BaseSettings):
    """this is a model of the settings for the app.

    Args:
        BaseSettings (_type_): this is the base class for the settings model
    """
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int 
    class Config:
        env_file = ".env"

settings = Settings()