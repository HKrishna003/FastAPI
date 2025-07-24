from sqlalchemy.orm import sessionmaker
from app.core.connect_db import create_connection
from app.schemes.user_details import User
from app.models.user_details import UserTable
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

async def add_user_db(user_data: User):
    try:
        engine = await create_connection()
        SessionLocal = sessionmaker(bind=engine)
        session = SessionLocal()

        new_user = UserTable(
            username=user_data.username,
            email=user_data.email,
            password=user_data.password
        )

        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        session.close()
        logger.info("User Added")
        return "User Added"
    
    except Exception as e:
        logger.error(e)
        return f"Error while adding user {e}"
