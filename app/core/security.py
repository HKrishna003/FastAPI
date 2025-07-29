from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "super-secret-key"
ALGORITHM = "HS256"

# Add custom payload
payload = {
    "sub": "123",                            # subject (user ID)
    "username": "hari_krishna",             # custom field
    "role": "admin",                        # custom field
    "exp": datetime.utcnow() + timedelta(minutes=30)  # expiration
}

# Encode JWT
token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

print(token)
