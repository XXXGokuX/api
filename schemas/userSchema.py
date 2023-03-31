from datetime import datetime
from pydantic import BaseModel

class UserCreate(BaseModel):
    id: int
    username: str
    password: str 
    created_at: datetime = datetime.now()


class UserOutput(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode= True


class UserSignin(BaseModel):
    username: str
    password:str

    
