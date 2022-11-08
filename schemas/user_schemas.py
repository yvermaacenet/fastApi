from pydantic import BaseModel


class User_Schemas(BaseModel):
    email:str
    password:str
