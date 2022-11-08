from pydantic import BaseModel


class Blog_Schemas(BaseModel):
    name: str
    email:str
