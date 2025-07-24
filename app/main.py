from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from contextlib import asynccontextmanager, contextmanager

from sqlalchemy import text
from app.core.connect_db import create_connection
from app.routes import add_user_route
from app.models.user_details import Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        engine = await create_connection()
        Base.metadata.create_all(bind=engine)
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
            print("✅ Successfully connected to the database.")
            print("Application Startup Complete")
    except Exception as e:
        print("Failed to start application: ", e)
    yield
    print("Application Closed Successfully")

app = FastAPI(lifespan=lifespan)


app.include_router(add_user_route.router)



