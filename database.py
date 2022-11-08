from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlalchemy
#SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
#SQLALCHEMY_DATABASE_URL = "mariadb+mariadbconnector://root:password@localhost:3308/acenetdatabase"
#SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:password@localhost:3308/acenetdatabase"
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:""@localhost:3306/dbacenet"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,  echo=False
)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, )
Base = declarative_base()
# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
