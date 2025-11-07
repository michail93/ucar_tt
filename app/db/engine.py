import os

from sqlalchemy.ext.asyncio.engine import AsyncEngine
from sqlmodel import create_engine

POSTGRES_USER = os.environ['POSTGRES_USER']
POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']
POSTGRES_DB = os.environ['POSTGRES_DB']

engine = AsyncEngine(
    create_engine(
        f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@db:5432/{POSTGRES_DB}",
        echo=True,
        future=True,
    )
)
