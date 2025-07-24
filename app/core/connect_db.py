from sqlalchemy import create_engine
from app.core.config import Settings

settings = Settings()

async def create_connection():
    username = settings.DB_USER
    password = settings.DB_PASS
    database_name = settings.DB_NAME

    # Example using pymysql
    connection_url = f"mysql+pymysql://{username}:{password}@localhost:3306/{database_name}"
    engine = create_engine(connection_url)
    return engine
