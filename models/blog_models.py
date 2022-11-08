
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base

class Blog_Models(Base):
    __tablename__ = "blog_model"
    id = Column(Integer, primary_key=True )
    name = Column(String(50))
    email = Column(String(50), unique=True, index=True)
     