from pydantic import BaseModel


class Authentication_Schemas(BaseModel):
    username:str
    password:str
