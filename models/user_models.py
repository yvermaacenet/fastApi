
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base

class User_Models(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True )
    email = Column(String(50), unique=True, index=True)
    password = Column(String(200))
     