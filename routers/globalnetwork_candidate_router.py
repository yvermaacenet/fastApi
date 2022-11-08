from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas import globalnetwork_candidate_schemas, user_schemas
from repository import globalnetwork_candidate_repository
from oauth2 import get_current_user
router = APIRouter(
    prefix="/globalnetwork_candidate",
    tags=['Candidate']
)


@router.post("/" )
def globalnetwork_candidate(request: globalnetwork_candidate_schemas.Globalnetwork_Candidate_Schemas , db: Session = Depends(get_db)):
    return globalnetwork_candidate_repository.Post_Globalnetwork_Candidate_Data(request,db)
    
@router.get("/")
#def globalnetwork_candidate(db: Session = Depends(get_db), get_current_user: user_schemas.User_Schemas = Depends(get_current_user) ):
def globalnetwork_candidate(db: Session = Depends(get_db)):
    return globalnetwork_candidate_repository.Get_Globalnetwork_Candidate_Data(db)
    