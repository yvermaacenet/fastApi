
from sqlalchemy.orm import Session
import models.blog_models as blog_models
from schemas import blog_schemas

def get_blogs_data(db: Session):
    get_blogs = db.query(blog_models.Blog_Models).all()
    return get_blogs

def post_blogs_data(request: blog_schemas.Blog_Schemas , db:Session):
    post_blogs = blog_models.Blog_Models(name=request.name, email=request.email)
    db.add(post_blogs)
    db.commit()
    db.refresh(post_blogs)
    return post_blogs
 
def put_blogs_data(id:int ,request: blog_schemas.Blog_Schemas , db:Session):
    db.query(blog_models.Blog_Models).filter(blog_models.Blog_Models.id == id).update(name=request.name)
    db.commit()    
    return "Updated Successfully!"
 