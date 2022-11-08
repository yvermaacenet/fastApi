from fastapi import HTTPException, status, Depends
from database import get_db
from sqlalchemy.orm import Session
import models.user_models as user_models
from schemas import user_schemas
from hashing import Hash


def get_user_data(db: Session):
    get_user = db.query(user_models.User_Models).all()
    return get_user

def post_user_data(request: user_schemas.User_Schemas , db:Session):
    post_user = user_models.User_Models(email=request.email, password = Hash.bcrypt_password(request.password))
    db.add(post_user)
    db.commit()
    db.refresh(post_user)
    return post_user