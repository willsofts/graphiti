import os
from functools import lru_cache
from typing import Annotated

from fastapi import Depends
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict  # type: ignore


class Settings(BaseSettings):
    openai_api_key: str
    openai_base_url: str | None = Field(None)
    model_name: str | None = os.environ.get('MODEL_NAME','gpt-5-mini')
    small_model_name: str | None = os.environ.get('SMALL_MODEL_NAME','gpt-5-nano')
    embedding_model_name: str | None = os.environ.get('EMBEDDING_MODEL_NAME','text-embedding-3-small')
    neo4j_uri: str
    neo4j_user: str
    neo4j_password: str

    model_config = SettingsConfigDict(env_file='.env', extra='ignore')


@lru_cache
def get_settings():
    return Settings()  # type: ignore[call-arg]


ZepEnvDep = Annotated[Settings, Depends(get_settings)]
