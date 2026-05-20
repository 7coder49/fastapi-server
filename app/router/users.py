from typing import Any

from fastapi import APIRouter
from app.model import User
from app.database import SessionLocal

router = APIRouter()

@router.post("/createUser")
def create_user(user: dict):
    db = SessionLocal()
    
    db_user = User(name=user['name'], dept=user['dept'], age=user['age'])
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return {
        "message": "User created successfully"
    }


@router.get("/getUsers")
def get_user():
    db = SessionLocal()
    
    db_users = db.query(User).all()

    return {
        "data": db_users,
        "message": "User fetched successfully"
    }

