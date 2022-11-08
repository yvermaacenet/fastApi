from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas import blog_schemas
from repository import blog_repository
from models import blog_models
router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)


@router.post("/" )
def blog_post(request: blog_schemas.Blog_Schemas , db: Session = Depends(get_db)):
    return blog_repository.post_blogs_data(request,db)
    
@router.get("/")
def blog_get(db: Session = Depends(get_db)):    
    return blog_repository.get_blogs_data(db)

@router.get("/{id}")
def get_blog_by_id(id, db: Session = Depends(get_db)):
    blog = db.query(blog_models.Blog_Models).filter(blog_models.Blog_Models.id == id).first()
    return blog   

@router.delete("/{id}")
def delete_blog_by_id(id, db: Session = Depends(get_db)):
    db.query(blog_models.Blog_Models).filter(blog_models.Blog_Models.id == id).delete(synchronize_session = False)
    db.commit()
    return {"done"}   

@router.put("/{id}" )
def blog_update_by_id(id:int, request: blog_schemas.Blog_Schemas , db: Session = Depends(get_db)):
    return blog_repository.put_blogs_data(id, request,db)

        