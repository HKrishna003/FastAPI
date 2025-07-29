from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemes.user_details import User
from app.services.user_login_ser import user_check_db
from app.core.db_session import get_db  
import logging

from app.core.config import Settings

from jose import jwt
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

settings = Settings()

SECRET_KEY = settings.JWT_SECRET_KEY
ALGORITHM = settings.JWT_ALGORITHM

router = APIRouter(tags=["Login_user"])

@router.post("/login")
async def chek_user( email: str, password: str, db: AsyncSession = Depends(get_db) ):
    res = await user_check_db(email=email, password=password, db=db)
    # print(res.type())
    print("Res",res)
    if res.get("status") == "Login Successful":
        payload = {
            "user_id" : res.get("user_id",""),
            "user_name" : res.get("username",""),
            "email" : res.get("email",""),
            "exp": datetime.utcnow() + timedelta(minutes=30)
        }
    else:
         payload = {
            "user_id" : "",
            "user_name" : "",
            "email" : ""
        }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    print("Token", token)
    # print("Payload", payload)
    return {"status": res}



# Add custom payload
# payload = {
#     "sub": "123",                            # subject (user ID)
#     "username": "hari_krishna",             # custom field
#     "role": "admin",                        # custom field
#     "exp": datetime.utcnow() + timedelta(minutes=30)  # expiration
# }

# # Encode JWT
# token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

# print(token)

