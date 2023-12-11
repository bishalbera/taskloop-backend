from pymongo import MongoClient
from backend.database.config import settings


DATABASE_URL = f"mongodb+srv://{settings.database_username}:{settings.database_password}@{settings.database_name}.{settings.database_url}?retryWrites=true&w=majority"

client = MongoClient(DATABASE_URL)
