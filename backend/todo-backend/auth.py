from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
import os

# Get the JWT secret from environment
SECRET_KEY = os.getenv("JWT_SECRET", "your-super-secret-jwt-key-change-in-production")
ALGORITHM = "HS256"

security = HTTPBearer()

async def jwt_auth_middleware(request: Request, credentials: HTTPAuthorizationCredentials = security):
    token = credentials.credentials
    try:
        # Decode the JWT token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")

        # Add user info to request state
        request.state.user_id = user_id
        return {"user_id": user_id}
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")