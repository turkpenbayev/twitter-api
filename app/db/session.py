from typing import Optional, Generator

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker

from app.config import Settings

engine: Optional[Engine] = None
SessionLocal: Optional[sessionmaker] = None


def init(settings: Settings):
    global engine
    global SessionLocal
    uri = f'postgresql+psycopg2://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}'
    engine = create_engine(uri, pool_pre_ping=True)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    assert SessionLocal
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
