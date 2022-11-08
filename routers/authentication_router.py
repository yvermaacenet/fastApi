from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas import authentication_schemas
from repository import authentication_repository
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/login_auth",
    tags=['Authentication'])


@router.post("/" )
def user_post_auth(request: OAuth2PasswordRequestForm = Depends() , db: Session = Depends(get_db)):
    return authentication_repository.post_user_auth(request,db)
    
 