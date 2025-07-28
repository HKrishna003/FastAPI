from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemes.user_details import User
from app.services.user_login_ser import user_check_db
from app.core.db_session import get_db  
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)



router = APIRouter(tags=["Login_user"])

@router.post("/login")
async def chek_user( user_data: User, db: AsyncSession = Depends(get_db) ):
    res = await user_check_db(user_data=user_data, db=db)
    return {"status": res}
