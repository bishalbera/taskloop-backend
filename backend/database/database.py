

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from backend.database.config import settings


DATABASE_URL = f"mongodb+srv://{settings.database_username}:{settings.database_password}@{settings.database_name}.{settings.database_url}?retryWrites=true&w=majority"

engine = create_engine()
session = sessionmaker(autoflush=False, autocommit=False, bind=engine)

base = declarative_base()


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
