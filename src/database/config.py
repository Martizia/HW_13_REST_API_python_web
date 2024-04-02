from pydantic import ConfigDict, field_validator, EmailStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY_JWT: str
    ALGORITHM: str
    MAIL_USERNAME: EmailStr
    MAIL_PASSWORD: str
    MAIL_FROM: str
    MAIL_PORT: int
    MAIL_SERVER: str
    RADIS_DOMAIN: str = 'localhost'
    RADIS_PORT: int = 6379
    RADIS_PASSWORD: str

    @field_validator('ALGORITHM')
    @classmethod
    def validate_algorithm(cls, v):
        if v not in ['HS256', 'HS512']:
            raise ValueError("Algorithm must be HS256 or HS512")
        return v


    model_config = ConfigDict(extra='ignore', env_file=".env", env_file_encoding='utf-8') # noqa


config = Settings()
