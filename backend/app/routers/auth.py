from fastapi import APIRouter, HTTPException, Depends
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel
from app.models import User  # Assume a User model exists if needed
from app.database import SessionLocal

router = APIRouter()

class UserLogin(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(user: UserLogin, Authorize: AuthJWT = Depends()):
    db = SessionLocal()
    try:
        # For demonstration, we simply check for a fixed user.
        # In production, look up the user and compare hashed passwords.
        if user.username != "testuser" or user.password != "password":
            raise HTTPException(status_code=401, detail="Invalid credentials")
        access_token = Authorize.create_access_token(subject=user.username)
        return {"access_token": access_token}
    finally:
        db.close()
