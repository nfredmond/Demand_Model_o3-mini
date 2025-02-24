import os
from fastapi import HTTPException, Header
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/transportation_db")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Authentication dependency (simple header-based for demonstration)
def get_current_user(authorization: str = Header(...)):
    if authorization != "Bearer secret-token":
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {"username": "testuser", "id": 1}

# Database session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
