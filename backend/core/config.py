import os
import secrets
from typing import List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, HttpUrl, validator


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    INPUT_DATASET_DIR: Optional[str] = 'datasets'
    OUTPUT_DATASET_DIR: Optional[str] = 'client_data'

    # logs configs
    LOG_FILE_NAME: str = 'server.log'
    LOG_MAX_BYTES: int = 2000
    LOG_BACKUP_COUNTS: int = 10

    SECRET_KEY: str = secrets.token_urlsafe(32)
    SERVER_NAME: str = None
    SERVER_HOST: AnyHttpUrl = None
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    PROJECT_NAME: str
    SENTRY_DSN: Optional[HttpUrl] = None

    @validator("SENTRY_DSN", pre=True)
    def sentry_dsn_can_be_blank(cls, v: str) -> Optional[str]:
        if len(v) == 0:
            return None
        return v

    class Config:
        case_sensitive = True
        env_file = '.env'


settings = Settings()
