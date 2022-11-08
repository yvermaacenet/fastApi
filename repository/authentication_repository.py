from fastapi import HTTPException, status, Depends
from database import get_db
from sqlalchemy.orm import Session
import models.user_models as user_models
from schemas import authentication_schemas
from hashing import Hash 
from datetime import datetime, timedelta
from typing import Union
from JWTtoken import create_access_token , ACCESS_TOKEN_EXPIRE_MINUTES
def post_user_auth(request: authentication_schemas.Authentication_Schemas , db:Session = Depends(get_db)):
    auth_user = db.query(user_models.User_Models).filter(user_models.User_Models.email == request.username).first()
    if not auth_user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Invailed Credentials")

    if not Hash.verify_password(request.password , auth_user.password):
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Incorrect Password") 
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": auth_user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
   
 