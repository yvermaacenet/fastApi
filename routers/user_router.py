from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas import user_schemas
from repository import user_repository
from models import user_models
from oauth2 import get_current_user

router = APIRouter(
    prefix="/user",
    tags=['Users']
)


@router.post("/" )
def user_post(request: user_schemas.User_Schemas , db: Session = Depends(get_db)):
    return user_repository.post_user_data(request,db)
    
@router.get("/")
# def user_get(db: Session = Depends(get_db), get_current_user: user_schemas.User_Schemas = Depends(get_current_user)):    
def user_get(db: Session = Depends(get_db)):    
   return user_repository.get_user_data(db)
